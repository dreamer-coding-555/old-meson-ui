/************************************************
 * author:  Michael Brockus.                   *
 * license: Apache Software License            *
 * @gmail: <mailto:michaelbrockus@gmail.com>    *
 ************************************************/
#include <cassert>
#include <list>
#include <iterator>
#include <algorithm>

#include "palindrome.h"
#include "compress.h"
#include "UnitTest++.h"

template <typename T>
bool operator==(const std::list<T> &lhs, const std::list<T> &rhs)
{
    return std::equal(lhs.begin(), lhs.end(), rhs.begin());
}

SUITE(PalindromeFunction)
{
    typedef std::list<int> list;

    TEST(_Palindrome_caseOne)
    {
        //
        // here we try an empty STL list
        const list data;
        CHECK(palindrome(data.begin(), data.end()) == false);
    }

    TEST(_Palindrome_caseTwo)
    {
        //
        // here an STL list containing an odd number element
        // form a palindrome
        const list data{1};
        CHECK(palindrome(data.begin(), data.end()) == true);
    }

    TEST(_Palindrome_caseThree)
    {
        //
        // here STL list containing an even number of
        // elements that form a palindrome
        const list data{1, 2, 3, 4, 4, 3, 2, 1};
        CHECK(palindrome(data.begin(), data.end()) == true);
    }

    TEST(_Palindrome_caseFour)
    {
        //
        // next an STL list containing an odd number of
        // elements that form a non-palindrome
        const list data{1, 2, 3, 4, 5};
        CHECK(palindrome(data.begin(), data.end()) == false);
    }

    TEST(_Palindrome_caseFive)
    {
        //
        // here a STL list containing an even number of
        // elements that form a non-palindrome
        const list data{1, 2};
        CHECK(palindrome(data.begin(), data.end()) == false);
    }

    TEST(_Palindrome_caseSix)
    {
        //
        // 1. First example
        const list data{1, 2, 3, 4, 3, 2, 1};
        CHECK(palindrome(data.begin(), data.end()) == true);
    }

    TEST(_Palindrome_caseSeven)
    {
        //
        // 2. Second example
        const list data{1, 2, 3, 4, 5, 6, 7};
        CHECK(palindrome(data.begin(), data.end()) == false);
    }
}

SUITE(CompressFunction)
{
    typedef std::list<int> list;
    TEST(_Compress_caseOne)
    {
        //
        // we use an empty STL list
        const list expected;
        const list source;
        list result;

        compress(source.begin(), source.end(), std::back_inserter(result));
        CHECK(result == expected);
    }

    TEST(_Compress_caseTwo)
    {
        //
        // followed by a non-empty STL list containing
        // no consecutive duplicates
        const list source{1, 2, 3, 1, 2, 3};
        list result;

        compress(source.begin(), source.end(), std::back_inserter(result));
        CHECK(result == source);
    }

    TEST(_Compress_caseThree)
    {
        //
        // and at last a non-empty STL list containing
        // consecutive duplicates
        const list expected{1, 2, 1};
        const list source{1, 1, 2, 2, 1, 1};
        list result;

        compress(source.begin(), source.end(), std::back_inserter(result));
        CHECK(result == expected);
    }
}

int main(int, const char **)
{
    //
    // Run all of the Unit Tests
    return UnitTest::RunAllTests();
} // end of function main
