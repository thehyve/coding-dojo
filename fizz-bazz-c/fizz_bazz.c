#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>


char *fizbuzz(int nnn) {
    char *result;
    if (nnn % 3 == 0) {
        assert(asprintf(&result, "%s", "Fizz") >= 0);
    } else if (nnn % 5 == 0) {
        assert(asprintf(&result, "%s", "Buzz") >= 0);
    } else {
        assert(asprintf(&result, "%d", nnn) >= 0);
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
}

int main() {
    test_that_common_case_numbers_get_stringified();
    test_that_multiples_of_three_get_fizzed();
    assert_string_equal(fizbuzz(5), "Buzz");
}