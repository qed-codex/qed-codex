---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteEndpointTrim.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEndpointTrim.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEndpointTrim.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Trimming an endpoint's allocated word

Each unary count mark removes one zero from the front of the allocated word.
The empty count ends the scan, leaving the remaining word in its original order.


### `routine`

 Trim one leading zero from the destination per unary count mark, rejecting malformed marks
or destination bits. 

### `run`

 Removing each zero costs a count pop, a word pop, and a return. One
final empty count pop terminates the loop. Only the two named stacks change. 
