---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryEntryShadow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryEntryShadow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryEntryShadow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The proof shadow erases exactly the five suspended caller words. Actual
query sources, reusable workspace, reference and temporary bytes are retained.
No length premise is imposed on any erased word; this module constructs no
execution and changes no instruction table. 

### `erase`

 This is exactly the shadow used by the actual query's replay theorem. 

### `visible`

 Visible words retain their complete bit strings. 

### `blank`

 Erasure preserves an existing blank, whether or not the word is carried. 

### `cleanWork`

 The actual lower-bank clean-work predicate needs only its existing blanks. 

### `sources`

 All five immutable frontend source fields are visible to the shadow. 

### `marked_discarded`

 The marked return restores workspace outside the five collector ports.
In particular the actual reference321 is not required to be blank. 

### `accepted_discarded`

 The accepted return retains its separate output788 exception. 

### `word_bound`

 Only visible input bytes enter the local query width. 

### `erase_eq_literal`

 The literal predicate used by the actual staged-entry cap is the same
five-word shadow, including the two lower collector words. 

### `record_hidden_bound`

 The actual marked-record entry bounds its five retained words from the
real caller and collector fields. No candidate/history bound is needed here:
trial normalization changes768 and source staging changes only its six ports. 
