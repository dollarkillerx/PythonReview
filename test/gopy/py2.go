/**
 * @Author: DollarKiller
 * @Description:
 * @Github: https://github.com/dollarkillerx
 * @Date: Create in 21:22 2019-10-31
 */

//libtest.go
package main

import "C"

var a int

func init() {
	a = 110
}

//export Set
func Set(c int) int {
	a = c
	return c
}

//export Get
func Get() int {
	return a
}

func main() {

}
