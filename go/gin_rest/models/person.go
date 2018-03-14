package models

import (
	db "../database"
)

type Person struct {
	Id        int    `json:"id" form:"id"`
	FirstName string `json:"first_name" form:"first_name"`
	LastName  string `json:"last_name" form:"last_name"`
}

func (p *Person) AddPerson() (id int64, err error) {
	rs, err := db.SqlDB.Exec("INSERT INTO person(first_name, last_name) VALUES (?, ?)", p.FirstName, p.LastName)
	if err != nil {
		return
	}
	id, err = rs.LastInsertId()
	return
}

func (p *Person) GetPersons() (persons []Person, err error) {
	persons = make([]Person, 0)
	rows, err := db.SqlDB.Query("SELECT id, first_name, last_name FROM person")
	defer rows.Close()

	if err != nil {
		return
	}

	for rows.Next() {
		var person Person
		rows.Scan(&person.Id, &person.FirstName, &person.LastName)
		persons = append(persons, person)
	}
	if err = rows.Err(); err != nil {
		return
	}
	return
}

func (p *Person) GetPerson() (person Person, err error) {
	err = db.SqlDB.QueryRow("select id, first_name, last_name from person where id=?", p.Id).Scan(&person.Id, &person.FirstName, &person.LastName)
	if err != nil {
		return
	}
	return
}

func (p *Person) DelPerson() (id int64, err error) {
	rs, err := db.SqlDB.Exec("delete from person where id=?", p.Id)
	if err != nil {
		return
	}
	id, err = rs.RowsAffected()
	if err != nil {
		return
	}
	return
}

func (p *Person) UpdatePerson() (id int64, err error) {
	rs, err := db.SqlDB.Exec("update person set first_name=?, last_name=? where id=?", p.FirstName, p.LastName, p.Id)
	if err != nil {
		return
	}
	id, err = rs.RowsAffected()
	if err != nil {
		return
	}
	return
}
