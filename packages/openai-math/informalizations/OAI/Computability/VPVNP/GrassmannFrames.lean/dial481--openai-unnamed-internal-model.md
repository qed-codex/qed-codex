---
{
  "module": "OAI/Computability/VPVNP/GrassmannFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Column moves for Grassmannian rigidity

In the equality case of Lemma 5.3 of *VP and VNP differ over every field*,
a column may be replaced by any vector outside the span of the entire tuple.
We show that these moves connect all ordered independent tuples with a fixed
initial segment when there is at least one unused ambient dimension.


### `OutsideStep`

 A free column is replaced by a vector outside the current span. Independence
of the extended tuple records both the original independence and the span condition. 

### `exists_outside_both`

 Two partial tuples of length less than the dimension admit a common new
column outside both spans, including over the binary field. 

### `connected`

 All independent tuples with a prescribed initial segment are connected by
moves that leave this segment fixed and insert a column outside the current span. 

### `connected_of_prefix`

 A length-indexed version of connectivity for a prescribed prefix. 

### `invariant`

 Any quantity preserved by outside-column replacements is constant on the
independent completions of a fixed tuple. 
