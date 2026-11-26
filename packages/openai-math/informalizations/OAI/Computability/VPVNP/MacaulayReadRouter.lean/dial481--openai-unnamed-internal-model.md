---
{
  "module": "OAI/Computability/VPVNP/MacaulayReadRouter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadRouter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayReadRouter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Calling the three physical Macaulay entry routines

The row descriptor selects an original coefficient, an affine pin coefficient,
or a powered-monomial equality test. The dispatch and selection code preserves
the caller's input addresses. Its running time is polynomial in the word
width. The long selected routine uses its own independent live-space bound.


### `ofTag`

 Decode tag 0 as an original equation, tag 1 as an affine pin and any larger tag as a
powered monomial. 

### `reader`

 One fixed instruction table, formed from the three coefficient routines. 

### `Params`

 Runtime size words occupy registers 2 through 7. Registers 0 and 1
refer to the caller's two address ports, and may change between reads. 

### `Ready`

 The private workspace contains the advised row counts and a coefficient bank satisfying the
caller's readiness predicate. 

### `ArmCorrect`

 A run of one coefficient routine from a populated row descriptor. The
three routines are called on disjoint classes of indices. Their bounds may
be exponential in time while keeping polynomial space. 

### `correctSpace_of_arms`

 The call interface consumed by the Gram and Schur engine, with all
routing and register framing accounted for. 
