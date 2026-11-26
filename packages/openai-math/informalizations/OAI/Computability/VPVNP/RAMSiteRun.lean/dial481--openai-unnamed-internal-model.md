---
{
  "module": "OAI/Computability/VPVNP/RAMSiteRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary paths of a site validator

The public bucket size bounds the number of calls independently of incoming
messages. The validator checks the input range before simulating the calls.
Its outgoing check compares an internal send with the actual result, or
requires acceptance on the terminal site. It consumes exactly the local binary
choices and fixed-width read guesses used by those calls.


### `runSite`

 Simulate the private calls assigned to this site, leaving the unused bits. 

### `validateSite`

 Exact-use site validator with the successor or terminal check. Later local
record and sorting checks can be applied to the returned reports. 

### `siteBitsEquiv`

 Any further deterministic check of the local reports preserves the exact
correspondence between valid reports and accepting binary inputs. 

### `boundedSiteBitsEquiv`

 The local path count is unchanged by restricting the ambient space of
reports to the finite domain used for the product of validator counts. 
