---
{
  "module": "OAI/Computability/VPVNP/LiveIncomingPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveIncomingPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveIncomingPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical incoming cuts in the live group count

Section 14.1 checks the padding of both incident cuts. The recurrence for
exponent vectors already checks a pair's outgoing padding, and a tail step
checks its outgoing configuration. Here those outgoing conditions imply
every incoming format check whenever the product of all groups is nonzero.
The incoming midpoint is a pair-format cut, even at the first tail group.


### `pairPadding`

 The trailing padding on an outgoing pair-format cut, at its physical sites. 

### `incomingChecks`

 The physical check on the input side of a group. The initial cut has
no condition. Up to the midpoint the incoming padding is checked. Later
incoming cuts must decode to canonical evaluator configurations. 

### `incomingChecks_pair`

 This includes the input of the first tail group, whose cut carries
exponents rather than a serialized evaluator state. 

### `incomingChecks_tail`

 A tail-format input passes exactly when its literal cut equals one of
the canonical mode/configuration/padding strings. 

### `incomingChecks_midpoint`

 The first tail group receives the last cumulative exponent vector.
It validates the midpoint's remaining bits using the first-half layout. 

### `pairCount_padding`

 Every nonzero pair factor enforces the physical zero-padding interval
of its output cut. 

### `tailCount_decoded`

 Every nonzero tail factor with an outgoing interior cut has produced a
decodable canonical configuration. 
