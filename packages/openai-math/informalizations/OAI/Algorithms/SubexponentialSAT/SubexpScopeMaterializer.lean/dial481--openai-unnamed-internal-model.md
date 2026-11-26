---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpScopeMaterializer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScopeMaterializer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScopeMaterializer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical scope-record iteration for candidate materialization

Scope indices use the existing `encodeList encodeNat` format. Candidate labels
form a flat stream of equally sized little-endian records. The record reader,
label extraction, chunk update, and validity accumulation are actual finite
programs; the list functions below specify their result.


### `tapes`

 Local materializer ports 0–9; scope 10; flat labels 11; unary record width 12;
label-extraction scratch 13–15; parsed payload 16; aggregate validity 17. 

### `patchChunks`

 Concrete list update used only to specify the array written by the machine. 

### `materialize_lookup`

 With distinct scope indices, each supplied local label occupies its own
chunk in the final stored array, in exactly the emitted scope order. 
