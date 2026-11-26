---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryShadow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryShadow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryShadow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The literal staged collector entry has a uniformly bounded proof shadow.
Only the five caller words left unrestricted by the query-time binder are
erased. No executable instruction, query evaluation, or semantic answer is
assumed in these physical input bounds. 

### `boundary_visible_bound`

 A candidate boundary has only three visible changing words: history,
framed counter, and the empty scratch. The incumbent and outer unary counter
remain completely unrestricted. 

### `trial_visible_bound`

 Normalization has the declared fixed payload width even for losing or
padded counter words. All other visible words retain their actual contents. 

### `staged_visible_bound`

 Actual trial staging copies only visible sources and prefixes the actual
candidate to the actual history. It does not copy any erased caller word. 

### `record_shadow_bound`

 At the real parser callback,321 is the current finite reference and
323/324 are empty. The unread tail320 and accumulated mass322 may have any
length; they disappear only in this proof-side shadow. 

### `marked_shadow_bound`

 This is the exact physical marked entry quantified by staged_rounds_eval.
All length assumptions concern the fixed prepared base and the explicitly
bounded history/candidate domain, never the five suspended caller words. 

### `marked_shadow_bound_of_references`

 The exact staged-round caller already bounds the complete encoded
reference stream. Its actual current reference is a member of that stream,
so no additional clause-count inequality is required. 

### `accepted_staged_visible_bound`

 History-only staging copies visible master words and physically clears
its temporary. It needs no bound on remaining caller counters. 

### `accepted_shadow_bound`

 The actual final RowBoundary suffices for the accepted entry shadow.
Its remaining-round word781 is unrestricted and erased, while the physical
history byte cap is retained. 
