#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdarg.h>

void safe_asprintf(char **ret, const char *format, ...) {
    va_list ap;
    va_start(ap, format);
    assert(vasprintf(ret, format, ap) >= 0);
    va_end(ap);
}

char *fizbuzz(int nnn) {
    char *result;
    //TODO Free the empty string in the heap
    safe_asprintf(&result, "");
    if (nnn % 3 == 0) {
        safe_asprintf(&result, "%s", "Fizz");
    }
    if (nnn % 5 == 0) {
        //TODO remove tmp pointer
        char *d = result;
        safe_asprintf(&result, "%s%s", result, "Buzz");
        free(d);
    }
    if (strlen(result) == 0) {
        safe_asprintf(&result, "%d", nnn);
    }
    return result;
}

void assert_string_equal(char *actual, char *expected) {
    if (strcmp(actual, expected)) {
        int print_status = printf("Assertion failed: got \"%s\", expected \"%s\"\n", actual, expected);
        assert(print_status >= 0);
    }
    free(actual);
}

void test_that_common_case_numbers_get_stringified() {
    assert_string_equal(fizbuzz(1), "1");
    assert_string_equal(fizbuzz(2), "2");
    assert_string_equal(fizbuzz(4), "4");
    assert_string_equal(fizbuzz(7), "7");
    assert_string_equal(fizbuzz(8), "8");
}

void test_that_multiples_of_three_get_fizzed() {
    assert_string_equal(fizbuzz(3), "Fizz");
    assert_string_equal(fizbuzz(6), "Fizz");
    assert_string_equal(fizbuzz(9), "Fizz");
}

void test_that_multiples_of_five_get_buzzed() {
    assert_string_equal(fizbuzz(5), "Buzz");
    assert_string_equal(fizbuzz(10), "Buzz");
}

int main() {
    test_that_common_case_numbers_get_stringified();
    test_that_multiples_of_three_get_fizzed();
    test_that_multiples_of_five_get_buzzed();
    assert_string_equal(fizbuzz(15), "FizzBuzz");
}
