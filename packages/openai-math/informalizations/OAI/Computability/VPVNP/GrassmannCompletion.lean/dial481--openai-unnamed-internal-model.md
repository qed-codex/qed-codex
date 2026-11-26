---
{
  "module": "OAI/Computability/VPVNP/GrassmannCompletion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannCompletion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannCompletion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Common completions of adjacent column frames

In the equality case of Lemma 5.3 of *VP and VNP differ over every field*,
one original column of a frame is replaced by a vector outside the span.
Putting the difference between the two columns into the completion preserves
the completed span of either block. Over the binary field this difference is
the sum used in Section 5.1.


### `completed_span_update`

 If the difference of two choices of a column already belongs to the
completion space, every completed block span is independent of the choice. 

### `independent_completed_update`

 Adding a completion column to an original column is an invertible
elementary operation on the completed frame. 

### `adjacent_commonCompletion`

 A common independent completion of the old and new frames containing
their column difference. The final equality holds for every block of columns,
including the whole tuple. 

### `binary_pair_commonCompletion`

 For the two original blocks of Section 5.1 over the binary field, the
common completion has exactly `m - r` columns and contains `v i + z`.
It preserves each of the two completed planes. 
