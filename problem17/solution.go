package main

import (
    "fmt"
    "strconv"
)


var units = map[int]string{
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
    6: "six", 7:"seven", 8:"eight", 9: "nine", 10: "ten", 
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen",
}

var tens = map[int]string{
    2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 
    6: "sixty", 7:"seventy", 8:"eighty", 9: "ninety",
}


func print_number(number int) {
    if number < 20 {
        fmt.Println(units[number])
    } else {
        var number_str = strconv.Itoa(number)
        var first_number,_ = strconv.Atoi(number_str[0:1])
        var remainder_number, _ = strconv.Atoi(number_str[1:len(number_str)])
        var first_word = ""
        if (len(number_str) == 3){
            first_word = units[first_number] + " hundred"
        }
        if (len(number_str) == 2){
            first_word = tens[first_number]

        }
        fmt.Print(first_word,  " ")
        print_number(remainder_number)


        //for _, r := range number_str {
        //    fmt.Println(string(r))
       // }
    }
}

func main() {
    for i := 1; i < 400; i++ {
        print_number(i)
    }
}
    
    

