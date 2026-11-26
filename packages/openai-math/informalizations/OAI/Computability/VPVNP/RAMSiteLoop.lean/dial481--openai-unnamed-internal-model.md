---
{
  "module": "OAI/Computability/VPVNP/RAMSiteLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming the private choices of a site

The site starts calls until its incoming state halts or the cumulative charge
reaches the next bucket. A call may cross that boundary, subject to the three
remaining charge limits. Each call leaves a suffix for its successor.


### `collectCall`

 Continue from the unused suffix and keep the current call's report. 

### `runSiteLoop`

 Execute consecutive charged calls in a bucket. `steps` bounds the number
of calls and `siteLeft` bounds their total startup and probe charges. 

### `runSiteLoop_iff`

 The loop uses precisely the binary guesses of the successful reports. It
may return a running state only at or past the next bucket boundary. 
