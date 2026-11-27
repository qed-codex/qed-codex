---
{
  "module": "OAI/Computability/VPVNP/ClassSeparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Informalization of OAI/Computability/VPVNP/ClassSeparation.lean: from the library's classes to the classes of the challenge

**This file contains a six-line proof of the one theorem that the challenge file states: over every field, VP and VNP are not the same class, for families that have $2n$ variables at index $n$. The proof rests on three results of the library: a theorem of the same shape for the library's own definitions of the two classes, and two lemmas that say that the definitions named in the statement are equivalent to the library's. This file puts the three together. The mathematics is in the modules behind that library theorem.** I have not checked that the file compiles, or what the three results rest on.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 29 lines. It imports two modules of the library, `Separation` and `Valiant.Project`. [Lines 1–2](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L1-L2) It has one theorem, `OAI.Computability.VPVNP.Standalone.vp_ne_vnp`. Its statement has the same text as the statement in the challenge file: I compared lines 14 to 17 here with lines 51 to 54 there, and they are equal. Its proof body does not contain `sorry`. [Lines 14–23](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L14-L23) [ComparatorChallenges/VPVNP.lean, lines 51–55](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.lean#L51-L55) This file does not import the challenge file, so the names in its statement refer to definitions of the library. A Comparator configuration names this file as the solution module. [VPVNP.json, line 3](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.json#L3)

## The three ingredients

1. **The library's separation.** `VPVNP.vp_ne_vnp` says that the library's own `IsVP` and `IsVNP` are different properties of families with the variables $(i, b)$, $0 \le i < n$, over every field. Its comment says that the family on the paired variables separates the two nonuniform classes over each field. [Separation.lean, lines 26–29](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L26-L29)
2. **VP agrees.** `Valiant.Project.isVP_iff` says that `Valiant.Project.IsVP p` holds exactly when `VPVNP.IsVP p` holds. I read the first as the class that the statement names and the second as the library's own. Its comment says that a polynomial bound on realizable table sizes is equivalent to a bound on the project's minimum gate counts. [Valiant/Project.lean, lines 15–17](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Valiant/Project.lean#L15-L17)
3. **VNP agrees.** `Valiant.Project.isVNP_iff` says the same for VNP. Its comment says that identical Boolean witness substitutions and the same size bounds give identical VNP classes. [Valiant/Project.lean, lines 27–28](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Valiant/Project.lean#L27-L28)

## The proof

Suppose the two properties that the statement names were equal. Take any family $f$. By ingredient 2, $f$ is in the library's VP exactly when it is in the VP of the statement. By the assumption, that holds exactly when $f$ is in the VNP of the statement. By ingredient 3, that holds exactly when $f$ is in the library's VNP. So the library's two properties agree on every family, and are therefore equal. This contradicts ingredient 1. [Lines 18–23](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L18-L23)

The step from "agree on every family" to "equal" uses `funext` and `propext`. `propext` is an axiom. `funext` is a theorem of Lean's core library that rests on the axiom `Quot.sound`. Both axioms are among the three that the Comparator configuration permits. I have not checked which axioms the whole proof uses. [Lines 20–21](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ClassSeparation.lean#L20-L21) [VPVNP.json, lines 8–12](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.json#L8-L12)

## Where the library's separation comes from

`Separation.lean` has 40 lines and three theorems. [Separation.lean, lines 1–40](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L1-L40) Its opening comment says that the explicit family is treated in `explicit_complete_family`, that a fixed compressed-pair compiler closes the diagonal argument, and that the threshold is chosen for each exponent and characteristic before the field is chosen. [Separation.lean, lines 4–10](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L4-L10)

- `separation_lower_bound`, which its comment calls the uniform exact arithmetic circuit lower bound of Theorem 1.1. For every natural number $C \ge 1$ and every characteristic $q$ there is an $N$ such that, for all $n \ge N$ and every field of characteristic $q$, the image over that field of a certain integer polynomial $P_n$ has `circuitSize` more than $n^C$. Here $q$ is any natural number, and the statement says nothing unless $q$ is $0$ or a prime. Its proof has three lines and calls `FixedProgramDiagonal.uniform_of_pair_compilers` and `paperPairCompiler`. [Separation.lean, lines 18–24](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L18-L24)
- `vp_ne_vnp`, ingredient 1, which is derived from that lower bound by a lemma called `vp_ne_vnp_of_uniform_P`. [Separation.lean, lines 26–29](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L26-L29)
- `corollary12`, which its comment calls Corollary 1.2. For every natural number $C$, zero included, it gives a lower bound of the same kind for the polynomial of directed Hamiltonian cycles and, outside characteristic $2$, for the permanent. It is not used in this file. [Separation.lean, lines 31–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Separation.lean#L31-L36)

The lower bound puts the family $P_n$ outside the library's VP. The separation also needs that this family is in the library's VNP. I did not read where that is shown. It would be in or behind `vp_ne_vnp_of_uniform_P`. The challenge statement keeps only the consequence for the two classes.

## What this file does not show

- **The mathematics.** It is behind the lemmas that the proof of `separation_lower_bound` calls and behind `vp_ne_vnp_of_uniform_P`. I did not read those, and I did not check the modules behind them for `sorry` or for the axioms they use. The folder `OAI/Computability/VPVNP` has 3,146 files at this revision.
- **That the definitions match.** The statement has the same text as the statement of the challenge. The definitions that it names, `Valiant.Project.Family`, `IsVP` and `IsVNP`, come from a library module that I did not read. To check that these agree with the definitions of the challenge is the task of a Comparator run, and I have not run one.
- **What the polynomial $P_n$ is.** This note does not say. Its definition is in the library.
- **That the build succeeds.** I have not built the project and have not run Comparator. The configuration sets `enable_nanoda` to `false`. [VPVNP.json, line 13](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/VPVNP.json#L13) In Comparator, setting that switch to `true` adds a check with a second kernel, nanoda, to the check with Lean's own kernel. [Comparator README, lines 12–13](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L12-L13) [Comparator README, lines 86–87](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L86-L87)

## What I read

I read this file, the challenge file, its Comparator configuration and `Separation.lean` in full, and lines 1 to 33 of `Valiant/Project.lean`, at the linked revision. These include the proofs of the two equivalence lemmas, which call further lemmas that I did not read. I read the lines of the Comparator README that describe the second kernel. I counted the files of the folder from the repository's file list. I did not read any other module of the library. I did not read the manuscript, and I did not build the project.
