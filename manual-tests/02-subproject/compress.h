/************************************************
 * author:  Michael Brockus.                   *
 * license: Apache Software License            *
 * @gmail: <mailto:michaelbrockus@gmail.com>    *
 ************************************************/
#ifndef COMPRESS_H
#define COMPRESS_H

//
// compress accepts a forward iterator range [first, last) and an output iterator.
// compress copies the elements from the iterator range to the output iterator
// eliminating all consecutive duplicates.
template <typename ForwardIterator, typename OutputIterator>
void compress(ForwardIterator first, const ForwardIterator last, OutputIterator result)
{
	//
	// here we check to see if the first forward
	// iterator is not equal to the last forward
	// iterator, and if not we will do the following.
	if (first != last)
	{
		*result = *first;
		//
		// we run an infinite loop so we can process
		// the values.
		while (true)
		{
			bool different = (*first != *(++first));
			//
			// here if first forward iterator is the same
			// as forward iterator we just skip are process.
			// else we do are work.
			if (first == last)
			{
				break;
			}
			else if (different)
			{
				++result;
				*result = *first;
			}
		}
	}
}

#endif