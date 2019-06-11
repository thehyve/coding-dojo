#include <stdio.h>
#include <assert.h>
#include <string.h>


char *fizbuzz(int nnn) {
    char *result;
    assert(asprintf(&result, "%d", nnn) >= 0);
    if (nnn == 3) {
        return "Fizz";
    }
    return result;
}

void assert_string_equal(char *actual, char *expected) {
    if (strcmp(actual, expected)) {
        int print_status = printf("Assertion failed: got \"%s\", expected \"%s\"\n", actual, expected);
        assert(print_status >= 0);
    }
}

void test_that_common_case_numbers_get_stringified() {
    assert_string_equal(fizbuzz(1), "1");
    assert_string_equal(fizbuzz(2), "2");
    assert_string_equal(fizbuzz(4), "4");
}

int main() {
    /* TODO: deallocate strings after asserting */
    test_that_common_case_numbers_get_stringified();
    assert_string_equal(fizbuzz(3), "Fizz");
}
