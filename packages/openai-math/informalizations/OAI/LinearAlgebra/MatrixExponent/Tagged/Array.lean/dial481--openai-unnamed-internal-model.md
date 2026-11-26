---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Tagged/Array.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Tagged/Array.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Tagged/Array.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Checking sorted order with linear overhead

Each subtree reports its first and last rows and a bit saying whether
it is sorted. A join compares just the two adjacent endpoints.


### `lex_compare`

 Two comparisons of the first component and one of the second suffice. 


# Array layouts on bundles of bits

A layout partitions the exterior positions into disjoint copies of a
record. Any permutation of records induces a free bit permutation.


 # Substituting a batch of independent queries 

### `Batch`

 Batch size counts vertices only. Powers have disjoint exterior bits. 


# Preparing distinctness queries

The input and proposed output each occupy half a list. A real record has
flag zero. When excluded from the signed subset, a record changes only
its flag. Its position tag still distinguishes it from every other dummy.


### `prepare`

 A linear map inserting the signed choice of flags. 


# Sorting with a permutation verifier

Sum over proposed tagged outputs, retaining their payloads. Checking
order by payload and then by tag leaves exactly one witness, even when
some payloads coincide.


### `Batch.openInput`

 Move the second block of exterior inputs to the output side. 

### `sort_of_tag`

 A batch of tagged permutation verifiers supplies the same number
of independent sorts with linear overhead in the cost of a comparison. 


# Verifying a permutation in payload slices

The positional tags are distinct, so two checks that agree on the tag
necessarily refer to the same input row.


### `project`

 Apply a function to both sets of payloads, preserving all tags. 
