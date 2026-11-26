---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean",
  "declarations": [
    "Formalism.HN.PframeLA1.final_real1",
    "Formalism.HN.frame_linear_algebra_first"
  ],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "CC-BY-4.0"
}
---

# Measuring the dimension missed by a family of linear maps

A useful way to read `frame_linear_algebra_first` is to start in the target space. Put all the chosen images together and take their orthogonal complement $W$. A vector in $W$ detects none of those images. The proof measures how much of a positive operator's trace can sit on $W$ in two ways, then compares the answers to bound $\dim W$. [The theorem and its choice of subspace](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L77-L84) · [The trace on that subspace](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L119-L136)

## The quantitative claim

Let $B_i:V_i\to H$ be a finite family of linear maps between finite-dimensional complex inner product spaces. Choose positive real weights $c_i$ and subspaces $N_i\subseteq V_i$. Write $D=\dim H$, $R=\sum_i\dim V_i>0$, $K_i=c_iB_i^*B_i$, and $Q=\sum_i c_i B_iB_i^*$. The squared Hilbert–Schmidt norm used here is $\|A\|_{\mathrm{HS}}^2=\operatorname{Re}\operatorname{tr}(A^*A)$. [Spaces, maps and weights](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean#L11-L17) · [The three operator definitions](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/CorankShare/StatementFR.lean#L9-L22)

Three bounds control three different effects. The total error $\sum_i\|K_i-I\|_{\mathrm{HS}}^2$ is at most $eR$, where $0\le e\le1/4$. The total codimension of the $N_i$ is at most $\varepsilon R$. On the target side, writing $t=\operatorname{Re}\operatorname{tr}Q$, the hypothesis is $\operatorname{Re}\operatorname{tr}(Q^2)\le(1+\eta)t^2/D$, with $\eta\ge0$. For the orthogonal complement of the span of all $B_i(N_i)$, the conclusion is [the dimension estimate](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean#L18-L24)

$$\dim W\le D(\eta+4\varepsilon+4\sqrt e).$$

For example, if all three error parameters vanish, the estimate forces the chosen images to span $H$. When the coefficient of $D$ reaches one, the elementary inequality $\dim W\le D$ already gives the estimate. The proof disposes of $D=0$ with this inequality before dividing by $D$. [The conclusion](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/StatementFrameF.lean#L23-L24) · [The dimension-zero case](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L80-L83)

## Comparing the two traces

Choose an orthonormal basis $(g_j)$ of $W$ and sum the diagonal entries of $Q$ on it. Call the real part of this sum $u$. Expanding $Q$ gives $u=\sum_{i,j}c_i\|B_i^*g_j\|^2$. Each $g_j$ is orthogonal to $B_i(N_i)$, so $B_i^*g_j$ belongs to $N_i^\perp$. This is where discarded source dimensions enter. The error estimate for $K_i$ and Cauchy–Schwarz across the indices give $u\le R(\varepsilon+\sqrt{\varepsilon e})$. Applying the corresponding estimate to complete bases of the $V_i$ gives $t\ge R(1-\sqrt e)\ge R/2$. [Expansion and orthogonality](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L119-L148) · [Summing the errors](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L149-L168) · [Full bases](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L96-L117) · [The bound on the square root](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L21-L26)

Now compare $Q$ with the scalar operator $(t/D)I$. Put $X=\|Q-(t/D)I\|_{\mathrm{HS}}^2$ and $w=\dim W$. The scalar operator contributes $(t/D)w$ on $W$, and the deviation costs at most $\sqrt{wX}$. Expanding the square gives $X=\operatorname{Re}\operatorname{tr}(Q^2)-t^2/D\le\eta t^2/D$. Thus a large missed space would require a large $u$, whereas the preceding source-space calculation bounds $u$ from above. [Lower estimate on the same trace](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L170-L186) · [The squared deviation](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L187-L219)

For the constants, $\varepsilon\ge1/4$ already gives a coefficient at least one. Otherwise put $y=D\sqrt X/t$, so $y^2\le\eta D$. Substituting the two bounds for $u$ and using $R/t\le2$ gives $w-\sqrt w\,y\le2D(\varepsilon+\sqrt{\varepsilon e})$. The inequality $2\sqrt w\,y\le w+y^2$ absorbs the term involving $\sqrt w$. Since $0\le\varepsilon<1/4$, we can bound $\sqrt{\varepsilon e}$ by $\sqrt e$, obtaining the displayed estimate. [Nonnegativity of the codimension parameter](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L85-L94) · [Normalization](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L22-L47) · [Eliminating the mixed term](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L48-L64) · [Application to the chosen subspace](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean#L220-L221)
