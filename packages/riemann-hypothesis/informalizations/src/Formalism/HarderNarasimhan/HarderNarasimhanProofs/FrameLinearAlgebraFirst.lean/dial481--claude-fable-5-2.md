---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean",
  "declarations": [
    "Formalism.HN.PframeLA1.final_real1",
    "Formalism.HN.frame_linear_algebra_first"
  ],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "CC-BY-4.0"
}
---

# Informalization of FrameLinearAlgebraFirst.lean: a bound on what the images of subspaces miss

**This file proves one fact of finite-dimensional linear algebra. Take linear maps $B_i : V_i \to H$ with positive weights $c_i$. Suppose the operators $c_i B_i^* B_i$ are close to the identity in total, and the weighted sum $\sum_i c_i B_i B_i^*$ is close to a multiple of the identity. Then the part of $H$ missed by the images of chosen subspaces of the $V_i$ has dimension at most an explicit multiple of $\dim H$. The multiple is small when three parameters are small: the two errors above and the total codimension of the subspaces.** The argument uses inner products, traces and the Cauchy–Schwarz inequality. The file’s three declarations all lie in the dependency closure of each of the five final theorems.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## The statement

The theorem `frame_linear_algebra_first` proves the proposition `FrameLA1`. [FrameLA1, lines 11–24](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean#L11-L24)

The data are a finite index set, finite-dimensional complex inner product spaces $V_i$ and $H$, linear maps $B_i : V_i \to H$, positive real weights $c_i$, subspaces $N_i \subseteq V_i$ (written `Nτ i` in the source) and real numbers $e$, $\eta$ and $\varepsilon$. Write:

- $R = \sum_i \dim V_i$ and $D = \dim H$;
- $Q = \sum_i c_i B_i B_i^*$, an operator on $H$ (`frQ c B` in the source);
- $\|A\|_2^2 = \operatorname{Re} \operatorname{tr}(A^* A)$, the squared Hilbert–Schmidt norm (`hs2 A`).

The source writes $c B^* B$ as `frK c B`. [The definitions, lines 9–22](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/StatementFR.lean#L9-L22)

Assume:

1. $R > 0$.
2. $\sum_i \|c_i B_i^* B_i - I\|_2^2 \le e R$ with $0 \le e \le \frac{1}{4}$. This bounds the total squared distance of the operators $c_i B_i^* B_i$ from the identity. A single $B_i$ may still be far from a scaled isometry, or zero: for a zero map the term is $\dim V_i$. [hilbert_schmidt_zero_map](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L161-L164)
3. $\operatorname{Re} \operatorname{tr}(Q^2) \le (1 + \eta) (\operatorname{Re} \operatorname{tr} Q)^2 / D$ with $\eta \ge 0$. Step 4 below shows that this bounds the distance from $Q$ to a multiple of the identity. Lean defines division by zero as zero, so the right side is $0$ when $D = 0$.
4. $\sum_i (\dim V_i - \dim N_i) \le \varepsilon R$. This bounds the total codimension of the subspaces $N_i$.

Then the orthogonal complement of the span of the images $B_i(N_i)$ has dimension at most a fixed multiple of $D$:

$$\dim \Big( \sum_i B_i(N_i) \Big)^{\perp} \le (\eta + 4 \varepsilon + 4 \sqrt{e}) D.$$

The multiple is small when $\eta$, $\varepsilon$ and $e$ are small. It can reach or exceed $1$, and the bound then says nothing.

## How the proof goes

Let $W$ be that orthogonal complement, $w = \dim W$ and $t = \operatorname{Re} \operatorname{tr} Q$. Choose an orthonormal basis $g_1, \dots, g_w$ of $W$. The proof bounds the number $t_W = \sum_l \operatorname{Re} \langle g_l, Q g_l \rangle$ from above and from below.

1. **The trace is large:** $t \ge R (1 - \sqrt{e})$. The lemma `fam_bound` says that for an orthonormal family $f_1, \dots, f_k$ in $V_i$, the number $c_i \sum_m \|B_i f_m\|^2$ differs from $k$ by at most $\sqrt{k} \|c_i B_i^* B_i - I\|_2$. The trace $t$ equals $\sum_i c_i \sum_m \|B_i v_m\|^2$ for an orthonormal basis $v_m$ of each $V_i$. Applying `fam_bound` to these bases and summing over $i$ with Cauchy–Schwarz and hypothesis 2 gives the bound. [Lines 96–117](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L96-L117) · [fam_bound](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/CorankShareProofs/SumNormSqLeHilbertSchmidt.lean#L87-L101)
2. **Upper bound:** $t_W \le \varepsilon R + R \sqrt{\varepsilon e}$. Here $t_W = \sum_i c_i \sum_l \|B_i^* g_l\|^2$. Each $g_l$ is orthogonal to $B_i(N_i)$, so $B_i^* g_l$ lies in $N_i^{\perp}$, and the lemma `W_upper` bounds the inner sum by $\sum_m \|B_i f_m\|^2$ over an orthonormal basis $f_m$ of $N_i^{\perp}$. Then `fam_bound` with $k = \dim V_i - \dim N_i$, Cauchy–Schwarz and hypotheses 2 and 4 give the bound. [Lines 119–168](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L119-L168) · [W_upper](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/CorankShareProofs/SumNormSqLeHilbertSchmidt.lean#L164-L184)
3. **Lower bound:** $t_W \ge (t / D) w - \sqrt{w} \sqrt{X}$, where $X = \|Q - (t / D) I\|_2^2$. This is the lemma `sum_re_inner_bound` applied to $Q - (t / D) I$. [Lines 170–186](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L170-L186) · [sum_re_inner_bound](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/CorankShareProofs/SumNormSqLeHilbertSchmidt.lean#L69-L85)
4. **$X$ is small:** expanding in an orthonormal basis of $H$ gives $X = \operatorname{Re} \operatorname{tr}(Q^2) - t^2 / D$, so hypothesis 3 is the inequality $X \le \eta t^2 / D$. [Lines 187–219](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L187-L219)
5. **Real arithmetic:** the lemma `final_real1` takes the four inequalities together with $0 \le w \le D$ and returns the conclusion. [Lines 15–64](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L15-L64)

Step 5 runs as follows. Since $e \le \frac{1}{4}$, step 1 gives $R \le 2 t$. If $\varepsilon \ge \frac{1}{4}$, the claim follows from $w \le D$. Otherwise put $y = (D / t) \sqrt{X}$, so that $y^2 \le \eta D$ by step 4. Steps 2 and 3 give $w - \sqrt{w} y \le 2 D (\varepsilon + \sqrt{\varepsilon e})$, and the inequality $\sqrt{w} y \le (w + y^2) / 2$ turns this into

$$w \le \eta D + 4 D (\varepsilon + \sqrt{\varepsilon e}) \le (\eta + 4 \varepsilon + 4 \sqrt{e}) D.$$

Before these steps the proof settles the case $D = 0$, where both sides of the conclusion are $0$, and derives $\varepsilon \ge 0$ from hypothesis 4. [Lines 81–94](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L81-L94) The lemma `final_real1` does not assume $\eta \ge 0$. It derives it from $0 \le X \le \eta t^2 / D$. [Lines 27–35](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L27-L35) A private lemma, `hs2_nonneg`, records that $\|A\|_2^2 \ge 0$. [Lines 71–75](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L71-L75)

## Where it is used

James Shore’s compiled dependency data records one declaration that refers to `frame_linear_algebra_first`. It is `frame_theorem_sharp`, which passes the theorem to `theoremFSharp_of` and obtains `TheoremFSharp`. [Line 388](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L388) · [Shore’s dataset, v0.2.1](https://github.com/james-shore/rh-proof-dependencies/releases/tag/v0.2.1)

The hypothesis `FrameLA1` is applied in the auxiliary theorem `thmF_place`, with $H = \mathbb{C}^{\kappa \oplus \kappa_1}$ and $V_i = \mathbb{C}^{\iota_i}$. [Lines 145–146](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L145-L146) The proof of `theoremFSharp_of` calls `thmF_place` with $\varepsilon = u / (u + \tau)$. [Line 311](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/TheoremFSharp.lean#L311)

The file that defines `hs2` and `frQ` also states a neighbouring proposition, `FrameLA`. It has the constant $2 \eta$ in place of $\eta$ and lacks the hypothesis $\eta \ge 0$. It is proved as `frame_linear_algebra_bound`, and the compiled data places both outside all five closures. [FrameLA, lines 29–45](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/StatementFR.lean#L29-L45) · [frame_linear_algebra_bound, lines 268–399](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/CorankShareProofs/SumNormSqLeHilbertSchmidt.lean#L268-L399)

This page covers this file only. It does not describe `TheoremFSharp` or the argument that uses it.
