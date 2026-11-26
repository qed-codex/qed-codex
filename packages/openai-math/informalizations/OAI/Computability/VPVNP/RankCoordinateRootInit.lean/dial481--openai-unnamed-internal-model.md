---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateRootInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateRootInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateRootInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Loading the two determinant roots from reusable advice

The static root registers and field parameters can be stored once in advice.
A fixed scan copies these stacks into fresh work ports before a pair of Schur
queries. The private matrix-reader ports are the only parts of the root banks
which depend on the live entry query.


### `load`

 Copy each advised template stack to its corresponding root port. 

### `loadClock`

 Bound the finite scan that copies all root stacks from advice, using the number of ports
and maximum saved stack height. 

### `load_runs`

 Runtime copying retains both the reusable sources and every stack outside
the chosen destinations. The space cap uses the initial height of all ports. 

### `RootHost`

 Full work-port type of the two streamed determinants, with the matrix reader's
private ports parameterized independently for numerator and denominator. 

### `template`

 Both engines start at the top coefficient of the degree-`r` pencil. Their
continuation stacks and result ports are empty. 

### `template_ready`

 The two root auxiliary banks meet the concrete determinant readers' readiness
conditions, including the binary matrix dimensions and packed field advice. 

### `readerPort`

 Location of a dynamic scalar-reader input within the paired root banks. 

### `setReaders`

 Filling the private reader inputs after loading the constant advice has
exactly the same effect as placing those inputs in the corresponding root banks. 

### `setReaders_mounted`

 The reader update can be made after the roots are mounted in a larger
workspace. Every engine port then sees its precise initialized value. 

### `templateCap`

 A uniform height bound for the fixed root template plus a scalar reader
whose own input stacks each have length at most `a`. 

### `template_total_length`

 Each advised word is counted once, even when different ports receive equal data. 

### `loadRoot_runs`

 Initialize the actual paired Schur workspaces in an empty scratch bank. Both
roots are installed at the top pencil query, and the copy's temporary port is
empty on return. The loaded template can be patched at `readerPort` with the
current entry request before the two determinant calls. 
