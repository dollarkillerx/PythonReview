/**
 * @Author: DollarKiller
 * @Description:
 * @Github: https://github.com/dollarkillerx
 * @Date: Create in 21:43 2019-10-31
 */

// http.go
package main

import (
	"C"
	"io/ioutil"
	"net/http"
)

// export Get
func Get(url *C.char) *C.char {
	urls := C.GoString(url)
	resp, err := http.Get(urls)
	if err != nil {
		return C.CString("")
	} else {
		defer resp.Body.Close()
	}
	bytes, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return C.CString("")
	}
	return C.CString(string(bytes))
}

func main() {

}
