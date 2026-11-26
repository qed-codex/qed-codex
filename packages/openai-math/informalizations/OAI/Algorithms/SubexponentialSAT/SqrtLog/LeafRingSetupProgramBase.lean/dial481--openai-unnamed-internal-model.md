---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramBase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramBase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafRingSetupProgramBase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The first concrete stage of ring setup.  Only the runtime binary
precision is supplied.  The generated scalar cache remains exposed while
the extension-ring table and constants are built.  The idempotent producer
later uses a separately framed preparation, with its own charged cost. 

### `scalarCommand_eval`

 This is an actual instruction trace from the one-word input, not an
assumption that a scalar cache or a modulus was supplied. 

### `scalarCall_eval`

 The local preparation executes on the declared physical ports. The
single input word is checked against the caller projection, and all other
caller tapes are framed by the actual lifted call. 

 Actual irreducible search followed by coefficient padding.  The model
below is the one selected by the finite search, not a supplied polynomial. 

### `searchCall_eval`

 Only the unary degree is initially present in the local search workspace.
The caller's modulus, scalar cache and width tapes lie outside that workspace. 

### `search_padding_ready`

 The raw search's scratch certificate is exactly sufficient for the
padding routine once the separately generated scalar-width word is copied
onto local12.  This statement is only a state-description lemma; the copy
itself is paid by `overwrite_eval`. 

### `paddingCall_eval`

 Padding is executed on the actual caller workspace.  Every stack other
than source13 and output21 is preserved, including the original degree14. 

 Table generation for the cache produced by the native scalar stage.
The cache is not replaced by a separately chosen mathematical cache. 

### `table_program_lifted`

 Every nonlocal register and stack is preserved by the actual lifted call. 

 Physical node generation and record framing at the ring-setup ports. 

 Actual constant-vector and idempotent calls in the setup workspace. 
