---
{
  "module": "OAI/Computability/VPVNP/RAMSortCorrect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCorrect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCorrect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Correctness of the bitonic record sort

At any threshold a bitonic block has one cyclic interval of ones. Opposite
comparisons produce a smaller and a larger pulse. Recursing sorts these into
the two halves of the correct output, whose one counts are determined by
truncating the old one count at half the block size. Thresholding then lifts
the Boolean result to any linearly ordered record type.


### `orderedBits`

 The Boolean block with `k` ones in the specified order. 

### `sort_bits`

 The network sorts every Boolean block into a single run of zeros and a
single run of ones in the requested order. 

### `sort_monotone`

 Batcher's ascending network sorts the entire block. 

### `sort_antitone`

 Odd-numbered intermediate blocks are sorted in descending order. 
