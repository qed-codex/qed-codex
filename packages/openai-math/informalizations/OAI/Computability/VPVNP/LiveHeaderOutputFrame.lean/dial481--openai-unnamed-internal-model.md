---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderOutputFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderOutputFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderOutputFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory passed from the live header into the nomination phase

The enclosing stage tag lies after the processor array and before header
scratch. Updating that tag preserves all decoded fields. The end of the
header allocation also gives the zero-initialization property used for the
auxiliary shadow, including after the nominations are stored.


### `Output.write_outer`

 Updating the outer dispatch cell keeps the complete physical output
image. Its value may change more than once before nominations begin. 

### `Output.fresh_after_limit`

 Unallocated scratch beyond the header stays at the RAM's zero default. 

### `Output.nomination_frame`

 Storing the nominated histogram preserves the header banks and leaves
every later address at the header's original zero default. 
