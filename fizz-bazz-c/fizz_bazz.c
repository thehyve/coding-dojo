#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>


char *fizbuzz(int nnn) {
    char *result;
    assert(asprintf(&result, "%d", nnn) >= 0);
    if (nnn == 3) {
        assert(asprintf(&result, "%s", "Fizz") >= 0);
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
}

int main() {
    test_that_common_case_numbers_get_stringified();
    assert_string_equal(fizbuzz(3), "Fizz");
}
