---
{
  "module": "OAI/Computability/VPVNP/LiveExponentFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveExponentFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frame and address guarantees for the linked exponent stage

The public bases are selected so the two input areas precede the carry
array, and all three arrays fit in the RAM address space. The native
program only changes the current label's carry. In particular its
continuing calls preserve the live-program dispatch tag.


### `layout_of_ranges`

 A numerical memory layout sufficient for the actual digit table.
The two read-only arrays may be separated by other scratch regions. 

### `frame_result`

 Continuing native calls advance the cursor within its range and
preserve any cell outside the entire carry array. 
