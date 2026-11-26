---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderFieldSuffix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldSuffix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderFieldSuffix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The full native incident-field suffix

The final sixteen scheduled stages alternate a private descriptor with a
bounded scan. The descriptors always run on the real width, mode and phase
words, and the scans read the original packed headers. Each accepted stage
hands off its actual final memory. Malformed padding yields a valid prefix
leading to a scan with no accepting continuation.


### `Bounds`

 Public bounds for these sixteen stages. 

### `Prepared`

 The descriptor output contains the requested offset and length, with only the tag and those
two scratch cells allowed to change. 

### `reach`

 Execute all descriptor/scan pairs whose indices precede the cursor.
The reachable image is strong enough to continue at the next pair. 

### `suffix_native`

 From the actual post-index, post-mode and post-primed memory, all sixteen
remaining stages accept on canonical padding, yielding every copied field
and the complete frame outside the occupied fields and three admin cells. 

### `bad_prefix_at`

 Reach a malformed padding scan after a valid prefix. Its entry retains
the actual headers and the offset/count words of the failing descriptor. 

### `first_bad_padding`

 Choose the first malformed side in the actual public order. 

### `bad_prefix`

 A malformed padding bit leads to a scheduled native scan at which no
choice tape and no fuel bound can produce an accepting exit. 
