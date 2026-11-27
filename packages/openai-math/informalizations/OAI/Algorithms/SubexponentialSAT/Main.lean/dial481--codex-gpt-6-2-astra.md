---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Where the SAT solution module gets its counting theorem

AI drafted this autoinformalization from the original source. It is open for mathematical review.

`Main.lean` has two imports. Its module note names `mainTheorem_explicit` as the main theorem of *A Subexponential Algorithm for Bounded-Width SAT*. It describes `exact_count_and_sat` as giving exact counting and a polynomial space bound at every prefix of the run. To find the proof term for the counting result, follow the second import into `SqrtLogSpace/Final.lean`. [Main.lean lines 1–16](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Main.lean#L1-L16) · [Final.lean lines 71–80](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L71-L80)

There the public statement asks for a primitive machine and two output tapes. The proof takes a compiled program and its run guarantee from `compiled_exact_count_and_sat`, uses `GuardedCompiler.primitive program` for the machine, and supplies two concrete tape numbers out of 1,220: 256 for the exact count and 1,216 for the yes-or-no answer. The same run guarantee supplies the time bound and bounds the space visited up to every intermediate point. [Final.lean lines 81–102](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L81-L102)

The quantifier order explains what is uniform. Choosing $k\ge 2$ fixes the machine and its constants. After that, changing the variable count or supplying another formula of width at most $k$ changes the input and the run, with the designated output tapes fixed. [Final.lean lines 74–90](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L74-L90)

I read the solution module and the cited declaration in its second import. I did not build the source or follow the compiler and running-time estimates back through their dependencies.
