<?php
/*
 * 把复杂的控制逻辑分解成有限个稳定状态，在每个状态上判断事件，变连续处理为离散数字处理，符合计算机的工作特点。
 * 同时，因为有限状态机具有有限个状态，所以可以在实际的工程上实现。但这并不意味着其只能进行有限次的处理，相反，有限状态机是闭环系统，有限无穷，可以用有限的状态，处理无穷的事务。

 * 状态机可归纳为4个要素，即 现态、条件、动作、次态。这样的归纳，主要是出于对状态机的内在因果关系的考虑。“现态”和“条件”是因，“动作”和“次态”是果。详解如下：

 * 现态：是指当前所处的状态。
 * 条件：又称为“事件”，当一个条件被满足，将会触发一个动作，或者执行一次状态的迁移。
 * 动作：条件满足后执行的动作。动作执行完毕后，可以迁移到新的状态，也可以仍旧保持原状态。动作不是必需的，当条件满足后，也可以不执行任何动作，直接迁移到新状态。
 * 次态：条件满足后要迁往的新状态。“次态”是相对于“现态”而言的，“次态”一旦被激活，就转变成新的“现态”了。
 *
 * 举个例子：人有三个状态健康，感冒，康复中。
 * 触发的条件有淋雨（t1），吃药（t2），打针（t3），休息（t4）。
 * 所以状态机就是：
 * 健康-（t4）->健康；
 * 健康-（t1）->感冒；
 * 感冒-（t3）->健康；
 * 感冒-（t2）->康复中；
 * 康复中-（t4）->健康，
 *
 *
 * 找出一个文本文件中所有符合条件的字符串（文本文件都是字母可能有回车，换行）
 * 文本文件str.txt如下：
 * sdfasdfAAAsAAAdfasddllfadsBBBsBBBdfdfdfsdfdf dfadfsfaHHHsKKKsaddfkkslslAAAAhBBBddfFFhMMM
 * 条件格式:
 * 1. 左边三个大写字母
 * 2. 中间一个小写字母
 * 3. 右边三个小写字母
 *
 * 解决这个问题涉及到栈(stack)结构, 后进先出
 *
 * +++++++++++++++++++++解题思路+++++++++++++++++++++++++++
 * 定义状态：对栈的情况定义相关的状态
 * 栈空状态： stat0,
 * 栈中一个有效数据：stat1
 * 栈中两个有效数据：stat2
 * 栈中三个有效数据：stat3
 * 栈中四个有效数据：stat4
 * 栈中五个有效数据：stat5
 * 栈中六个有效数据：stat6
 * 栈中七个有效数据：stat7
 *
 * 单个字符扫描文件让符合条件的字符入栈，根据栈的状态做出相应动作0.初始状态栈空，即$curState=0，遇到大写字母入栈，栈中一个有效字母，修改栈状态：$curState=1
 *
 * 当栈状态为1时，下一个字母必须为大写，才能入栈，否则置空栈，恢复栈状态：$curState=0
 * 当栈状态为2时，下一个字母必须为大写，才能入栈，否则置空栈，恢复栈状态：$curState=0
 * 当栈状态为3时，下一个字母必须为小写，才能入栈，否则置空栈，恢复栈状态：$curState=0
 * 当栈状态为4时，下一个字母必须为大写，才能入栈，否则置空栈，恢复栈状态：$curState=0
 * 当栈状态为5时，下一个字母必须为大写，才能入栈，否则置空栈，恢复栈状态：$curState=0
 * 当栈状态为6时，下一个字母必须为大写，才能入栈，否则置空栈，恢复栈状态：$curState=0
 * 当栈状态为7时，下一个字母必须为小写，此时栈中元素符合了有效条件格式，把栈中元素传给$box数组,然后置空栈，恢复栈状态：$curState=0；否则置空栈，恢复栈状态：$curState=0
 *
 * 必须考虑栈的当前状态与下一个状态成立间的关系，即现态与次态$box数组中就是文本文件中所有符合条件格式的字符串
 */
 

//状态数组   
$state = array('stat0', 'stat1', 'stat2', 'stat3', 'stat4', 'stat5', 'stat6', 'stat7');
//栈数组   
$shed = array();
//所有符合条件的字符   
$box = array();
//文件路径   
$file = 'd:/www/str.txt';
//当前状态 $state[0];
$curState = 0;
$handle = fopen($file, 'r');
while (!feof($handle)) {
    $string = fgetc($handle);
    if (ord($string) == 13 || ord($string) == 10) {
        continue; //遇到回车或换行跳过  
    }
    $case = $string == strtoupper($string) ? 'upper' : 'lower';
    //判断大小写         
    switch ($curState) {
        case 0:
            if ($case == 'upper') {
                array_push($shed, $string);
                $curState++;
            }
            break;
        case 1: if ($case == 'upper') {
                array_push($shed, $string);
                $curState++;
            } else {
                $shed = array();
                $curState = 0;
            } break;
        case 2: if ($case == 'upper') {
                array_push($shed, $string);
                $curState++;
            } else {
                $shed = array();
                $curState = 0;
            } break;
        case 3: if ($case == 'lower') {
                array_push($shed, $string);
                $curState++;
            } else {
                $shed = array();
                $curState = 0;
            } break;
        case 4: if ($case == 'upper') {
                array_push($shed, $string);
                $curState++;
            } else {
                $shed = array();
                $curState = 0;
            } break;
        case 5: if ($case == 'upper') {
                array_push($shed, $string);
                $curState++;
            } else {
                $shed = array();
                $curState = 0;
            } break;
        case 6: if ($case == 'upper') {
                array_push($shed, $string);
                $curState++;
            } else {
                $shed = array();
                $curState = 0;
            } break;
        case 7: if ($case == 'lower') {
                $box[] = $shed;
                $shed = array();
                $curState = 0;
            } else {
                $shed = array();
                $curState = 0;
            } break;
    }
}
echo '<pre>';
print_r($box);
