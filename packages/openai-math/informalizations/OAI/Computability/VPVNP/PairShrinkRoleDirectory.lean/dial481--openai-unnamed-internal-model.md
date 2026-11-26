---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decoding a shrinking visit from the popped row address

Each output site belongs to one occurrence of a selected term. Distinct
occurrences remain distinct even when the same term is chosen twice. The
parser receives only the popped word and scratch state. Its physical row
selects both the term occurrence and the site in that term's output network.


### `outputOrder`

 The order used when writing the rows of the chosen term's actual output network. 

### `Site`

 The second component is a site in the first component's term output. 

### `ShrinkSite`

 Only occurrences whose recorded kernel is a shrinking pass. 

### `outputTags`

 Turn the selected pass sequence into its output DFS layers, retaining the producing role of
each layer. 

### `siteRows`

 Numerical ordinals in a physical row are exactly the selected term's site order. 

### `address`

 Natural row address in the physical arena for a concrete chosen term and site. 

### `address_injective`

 Row addresses distinguish both the selected term occurrence and its output site. 

### `decode`

 Recover the shrink site from the physical node word. The decoder rejects
cursor rows, refresh rows, interiors of rows and addresses outside the row arena. 

### `decode_eq_some_iff`

 Successful decoding is equivalent to equality with the actual natural row address. 

### `decode_address`

 The physical word of each valid shrink row round-trips to its typed site.
The end may equal the word modulus because the allocated interval is half-open. 

### `parser`

 Select the parser for the actual shrinking site without passing any
level or owner as an additional input to the hook. 

### `read_at`

 The global reader returns exactly the local path and remaining bits
for the unique chosen site. This also identifies local and global rejection. 

### `Domain`

 Geometry and packet contents may vary with the selected output site. 

### `dispatch_at_site`

 The dispatcher's actual tag probe selects the recorded role of this site. 

### `domain_iff_dispatch`

 On genuine output rows, the typed shrink domain is the same domain as
the physical role guard, with the site's packet invariant preserved. 

### `exactOn`

 Assemble the genuine per-site native equivalences at their common
shrink entry and DFS continuation. Success and rejection use the same site. 
