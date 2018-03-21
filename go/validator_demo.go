import (
    "regexp"
    "fmt"
    "strings"
    "reflect"
)

// 声明struct标签常量
const tagName = "validate"

// 邮箱地址正则表达式
var mailRe = regexp.MustCompile(`\A[\w+\-.]+@[a-z\d\-]+(\.[a-z]+)*\.[a-z]+\z`)

// 验证器接口
type Validator interface {
    // 验证方法, 返回验证结果以及可选的error
    Validate(interface{})(bool, error)
}

// 默认验证器不实现任何验证方法
type DefaultValidator struct{

}

// 验证方法实现
func (v DefaultValidator) Validate(val interface{}) (bool, error) {
    return true, nil
}

// 数字验证器struct
type NumberValidator struct{
    Min int
    Max int
}

// 数字验证器方法
func (v NumberValidator) Validate(val interface{}) (bool, error) {
    num := val.(int)

    if num < v.Min {
        return false, fmt.Errorf("should be greater than %v", v.Min)
    }

    if v.Max >= v.Min && num > v.Max {
        return false, fmt.Errorf("should be less than %v", v.Max)
    }

    return true, nil
}

// 字符串验证器struct, 包含最大长度和最小长度两个属性
type StringValidator struct {
    Min int
    Max int
}

// 字符串验证方法
func (v StringValidator) Validate(val interface{}) (bool, error) {
    l := len(val.(string))

    if l == 0 {
        return false, fmt.Errorf("cannot be blank")
    }

    if l < v.Min {
        return false, fmt.Errorf("should be at least %v chars long", v.Min)
    }

    if v.Max >= v.Min && l > v.Max {
        return false, fmt.Errorf("should be less than %v chars long", v.Max)
    }

    return true, nil
}

// 邮箱验证器struct
type EmailValidator struct{

}

// 邮箱验证方法
func (v EmailValidator) Validate(val interface{}) (bool, error) {
    if !mailRe.MatchString(val.(string)) {
        return false, fmt.Errorf("is not a valid email address")
    }
    return true, nil
}

// 根据struct标签返回对应验证器
func getValidatorFromTag(tag string) Validator {
    args := strings.Split(tag, ",")

    switch args[0] {
    case "number":
        validator := NumberValidator{}
        fmt.Sscanf(strings.Join(args[1:], ","), "min=%d,max=%d", &validator.Min, &validator.Max)
        return validator
    case "string":
        validator := StringValidator{}
        fmt.Sscanf(strings.Join(args[1:], ","), "min=%d,max=%d", &validator.Min, &validator.Max)
        return validator
    case "email":
        return EmailValidator{}
    }

    return DefaultValidator{}
}

//Performs actual data validation using validator definitions on the struct
func validateStruct(s interface{}) []error {
    errs := []error{}

    //ValueOf returns a Value representing the run-time data
    v := reflect.ValueOf(s)

    for i := 0; i < v.NumField(); i++ {
        //Get the field tag value
        tag := v.Type().Field(i).Tag.Get(tagName)

        //Skip if tag is not defined or ignored
        if tag == "" || tag == "-" {
            continue
        }

        //Get a validator that corresponds to a tag
        validator := getValidatorFromTag(tag)

        //Perform validation
        valid, err := validator.Validate(v.Field(i).Interface())

        //Append error to results
        if !valid && err != nil {
            errs = append(errs, fmt.Errorf("%s %s", v.Type().Field(i).Name, err.Error()))
        }
    }

    return errs
}

type User struct {
    Id          int             `validate:"number,min=1,max=1000"`
    Name        string          `validate:"string,min=2,max=10"`
    Bio         string          `validate:"string"`
    Email       string          `validate:"string"`
}

func main() {
    user := User{
        Id: 0,
        Name: "superlongstring",
        Bio: "",
        Email: "foobar",
    }

    fmt.Println("Errors: ")
    for i, err := range validateStruct(user) {
        fmt.Printf("\t%d. %s\n", i+1, err.Error())
    }
}
