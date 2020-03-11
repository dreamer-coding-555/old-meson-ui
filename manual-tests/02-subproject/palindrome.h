/************************************************
 * author:  Michael Brockus.                   *
 * license: Apache Software License            *
 * @gmail: <mailto:michaelbrockus@gmail.com>    *
 ************************************************/
#ifndef PALINDROME_H
#define PALINDROME_H

#include <cassert>

// palindrome accepts a bidirectional iterator range [first, last) as input and
// returns true if the elements in the range form a palindrome (a sequence that
// reads the same forward and backward) and false otherwise.
template <typename BidirectionalIterator>
bool palindrome(BidirectionalIterator first, BidirectionalIterator last)
{
	//
	// here we check to see if the first forward
	// iterator is not equal to the last forward
	// iterator, and if not we will do the following.
	if (first == last)
	{
		return false;
	}
	else
		while (true)
		{
			--last;

			//
			// here we check to see if the derefrunced first
			// forward iterator is not equal to the last
			// derefrunced forward iterator, and if not we
			// will return false.
			if (*first != *last)
			{
				return false;
			}

			//
			// here we check to see if the first forward
			// iterator is equal to the last forward
			// iterator, and if not we will return true.
			if (first == last)
			{
				return true;
			}
			++first;
		}
}

#endif