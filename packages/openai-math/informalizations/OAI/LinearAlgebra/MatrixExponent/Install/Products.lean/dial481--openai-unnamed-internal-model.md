---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Install/Products.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/Products.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Install/Products.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Products of local weights on named bit indices 


# Sparse assignment

Candidate `i` has six possible links. In each synchronous round an
active candidate takes its first uncontested link, if any. No still
active candidate can subsequently use that target.



# Peeling sparse sets

Every reached target accounts for two links when links from retiring
sources are counted twice. This remains valid for parallel links.
Expansion therefore guarantees that at least a third of the sources retire.



# Deterministic sparse assignment

Only the activity bits and the six selected-link bits at each candidate
are stored. A retiring candidate takes its first uncontested link.
The invariant forbids every active candidate from hitting an occupied
target, so a later round can never reuse that target.



# Switching the payload after sparse assignment

Keep the activation mask separate from the payload bits, so only the
control bits need to pass through each round of the assignment algorithm.



# Oriented pairs of records

Both ends of a transport carry its identifier and its data. Flipping
the orientation bit must send each marked record to another marked
record. Unambiguous identifiers make the matching unique.



# Hiding the tags

For lists of distinct payloads, a proposed permutation has exactly one
valid assignment of positional tags. Summing over those tags therefore
works even over a field of positive characteristic.


### `recover`

 On a permutation of a distinct labelled list, erasure is invertible. 


# Checking opposite ends of transports

Compare the list of active records with the same list after reversing
orientation. Unmarked slots receive separate addresses. This keeps all
records distinct, so hiding positional tags introduces no multiplicities.


### `check_turns`

 One verifier on words suffices for a group of oriented transports. 
