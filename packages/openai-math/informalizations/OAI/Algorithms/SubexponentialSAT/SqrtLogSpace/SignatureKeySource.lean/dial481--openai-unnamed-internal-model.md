---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureKeySource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureKeySource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureKeySource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual full signature keys and the source head labels

The selected-coordinate list retains its physical order. The equivalence below
is the existing explicit selected-ID equivalence; it neither sorts assignments
nor replaces the full raw matrix by a basis.


### `ordered_signature`

 Reindexing the actual selected columns gives exactly the full integer
label used by source locality, with every original row retained. 

### `key_eq_freeLabel`

 Exact byte equality of keys computed from the ordered shifted matrix is
equivalent to equality of the full source labels. The coefficient premise is
the pointwise interpretation proved for the actual native loader output. 

### `naturalKey_eq_freeLabel`

 The actual binary cursor has the same full-key equality as the source
assignment obtained from the explicit selected-coordinate equivalence. 
