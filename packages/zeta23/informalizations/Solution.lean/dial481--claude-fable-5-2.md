---
{
  "module": "Solution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Informalization of Solution.lean: seventeen delegations and one identity about a constant

**This file restates the seventeen theorems of `Challenge.lean` and gives each a proof that hands it to a theorem of the Zeta23 library. Nine of the proofs are a single term. The other eight, the ones that involve the constant $c_1^*$, first rewrite the library's form of that constant into the form of the challenge. The rewriting rests on the one piece of mathematics proved in this file, an identity between two expressions for the constant.**

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 142 lines. Its header calls it the untrusted solution module and says that it holds the seventeen statements of `Challenge.lean`, each proved by delegating to the Zeta23 library. [Lines 6–8](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L6-L8) It imports `ChallengeDeps` and eight modules of the library. [Lines 32–40](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L32-L40) The header lists which library theorem each statement uses. [Lines 10–19](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L10-L19) It ends by saying that nothing in this file is part of the trusted base, because Comparator checks again that every theorem has the statement of its namesake in `Challenge.lean` and uses only the permitted axioms. [Lines 29–30](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L29-L30)

## Two sets of definitions

The statements in this file use the counting functions of `ChallengeDeps.lean`. The library has counting functions of its own. The header says that the two are the same character for character, in different namespaces, so that each delegation typechecks by unfolding definitions. [Lines 21–23](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L21-L23) The statements, at least, can be seen to match: the theorem `Zeta23.thmA₀` is written with the same formula as the theorem `two_thirds_on_critical_line` of this file, where the names in the library's formula are the library's own counting functions. [Zeta23/Final.lean, lines 293–298](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Final.lean#L293-L298) [Lines 52–54](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L52-L54) I did not compare the definitions themselves.

## The identity

The library writes the constant of Theorem D as `cStar 1`, where
$$c^*_\lambda = \frac{\sqrt{2} \sin\vartheta}{\cos\vartheta + \vartheta \sin\vartheta}, \qquad \vartheta = \lambda/\sqrt{2}.$$
[Zeta23/ThmD/Functional.lean, lines 28–29](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean#L28-L29) [Zeta23/ThmD/Functional.lean, lines 34–36](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean#L34-L36) The challenge writes it as `cMT`, the form with the tangent at $\vartheta = 1/\sqrt{2}$. The header calls the library's form division-safe. [Lines 24–27](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L24-L27) The library explains the word: this form is the tangent form multiplied through by $\cos\vartheta$, and its denominator stays at least $3/4$ for $0 \le \lambda \le 1$. [Zeta23/ThmD/Functional.lean, lines 13–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean#L13-L17)

The theorem `cStar_one_eq_cMT` says that `cStar 1` equals `cMT`. Its proof uses a lemma of the library, `cStar_eq_tan_form`, which gives the tangent form for $0 \le \lambda \le 1$, and then unfolds the definitions. [Lines 44–50](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L44-L50) [Zeta23/ThmD/Functional.lean, lines 228–231](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean#L228-L231)

The library also has names for the two constants of the bounds: `HD` is $2 - 1/c^*_\lambda$ and `GD` is $3/2 - 1/(2 c^*_\lambda)$. [Zeta23/ThmD/Functional.lean, line 53](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean#L53) [Zeta23/ThmD/Mult.lean, lines 380–381](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Mult.lean#L380-L381)

## The seventeen proofs

- **Nine direct ones.** Theorems A, B and C for the zeta function, in the dyadic and the cumulative form, are the library theorems `thmA₀`, `thmB₀_mult` and `thmC₀_mult` and their cumulative forms. [Lines 52–74](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L52-L74) The three bounds of Theorem E with the constants $2/3$ and $5/6$ are `thmE_A₀`, `thmE_B₀_mult` and `thmE_C₀_mult`, applied to the two hypotheses on $\chi$. [Lines 106–119](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L106-L119)
- **Eight with rewriting.** The five statements of Theorem D and the three statements of Theorem E with the constants of Theorem D each take a library theorem. By the header these are stated with the library's constants `HD 1` and `GD 1`. [Lines 13–19](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L13-L19) The proof unfolds that name and rewrites `cStar 1` to `cMT` by the identity. What remains is the statement of the challenge. [Lines 76–104](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L76-L104) [Lines 121–140](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Solution.lean#L121-L140)

## What this file does not show

- **The mathematics.** Apart from the identity, none of the argument is in this file. It is in the library, the folder `Zeta23`. That folder has 316 Lean files, some of them for other topics of the repository. The project has 326 in all.
- **That the two sets of definitions agree.** The header says so. Lean has to accept it when the project is built, and Comparator is the tool the project names for checking the statements against `Challenge.lean`. I have not built the project and have not run Comparator.
- **Agreement with the paper.** The project's metadata says that the trusted statement file was read against the paper by a paper author. [formalization.yaml, lines 27–28](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/formalization.yaml#L27-L28)

The labels A to E in this note are the repository's own, not the numbering of the paper. [README, lines 68–71](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/README.md?plain=1#L68-L71)

## What I read

I read this file and `Challenge.lean` in full. In the library I read the statement of `thmA₀`, the definitions of `theta`, `cStar`, `HD` and `GD`, and the statement of `cStar_eq_tan_form`. I did not read the other sixteen library theorems that this file names, and I read no proofs in the library. All of this is at the linked revision. I counted the Lean files of the project and of the folder `Zeta23`. I did not read the paper, and I did not build the project.
