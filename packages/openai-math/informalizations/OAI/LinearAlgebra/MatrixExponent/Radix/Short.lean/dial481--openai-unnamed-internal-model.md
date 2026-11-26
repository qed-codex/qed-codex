---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Radix/Short.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Short.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Short.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking a tagged permutation by sorting

Mark the labelled inputs and the proposed outputs with opposite bits.
Sort by the common address and payload, ignoring empty slots. Since
input labels are distinct, a permutation is characterized by consecutive
pairs with equal keys and opposite marks. Their order within a pair is free.


### `tag_of_sort`

 One sort of the marked union suffices. It uses twice the number of
live rows as payloads, leaving half of its slots empty. 


# Sorting a long key by stable digit passes

The last digits are sorted first. When an earlier digit is processed, each
sublist with that digit retains its order. A rewiring keeps the unused key
prefix attached to the suffix during the construction of each digit circuit.


### `radix`

 A pass can rearrange empty slots freely. Only its action on the real
records matters, and the occupancy bound is preserved by permutation. 


# Wider payloads at linear cost

Duplicate only the position tags when joining two verifiers. Payloads
go directly to the two networks, so recursive doubling incurs no
logarithmic factor in their total width.


### `widen`

 Split the payload into a dyadic number of slices and pad the last
slice. The overhead is uniform in the ratio of the two widths. 


# The wide-record recursion

It is enough to install calls at the threshold width. Once the height
ratio `τ` and width ratio `Y` are fixed, take the threshold exponent
`A` large enough that `τ^A ≤ Y`. Every recursive call then still
meets the wide-record threshold. Slicing handles widths above it.

