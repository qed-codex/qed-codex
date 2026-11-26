---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CanonicalFlagExistsUniqueSemistable.lean",
  "declarations": [
    "GlobalTheory.PointFlag.flag_spec"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A canonical flag from normalized lattice sizes

[Theorem ARAK.0233](https://andrewodesky.com/rh/lean/GlobalTheory.PointFlag.flag_spec/)

Fix the unitary lattice data and a point $x$ described below. Write $\Lambda=\Lambda_x$, $\rho=\rho_x$, $f=|\operatorname{Inf}(E)|$, and $\Delta=|\operatorname{disc}E|$. For an $\mathcal O_E$-submodule $A\subseteq E^n$, put $r(A)=\dim_E(EA)$ and $$s(A)=\left(2^{fr(A)}\Delta^{-r(A)/2}\operatorname{covol}(\rho(A))\right)^{1/(2fr(A))}.$$ For $B\subseteq A$, put $$s(A/B)=\left(2^{f(r(A)-r(B))}\Delta^{-(r(A)-r(B))/2}\operatorname{covol}(\operatorname{pr}_{\rho(B)^\perp}\rho(A))\right)^{1/(2f(r(A)-r(B)))}.$$ Saturation means $\rho(B)=\rho(A)\cap\operatorname{span}_{\mathbb R}\rho(B)$. Define $$s_{\min}=\inf_{0\ne A\subseteq\Lambda}s(A),\qquad s_{\max}(A)=\sup_{\substack{B\subsetneq A\\B\text{ saturated in }A}}s(A/B),$$ $$U_{\le t}=\sum_{\substack{0\ne A\subseteq\Lambda\\s_{\max}(A)\le t}}A,\qquad U_{<t}=\sum_{\substack{0\ne A\subseteq\Lambda\\s_{\max}(A)<t}}A.$$ All submodules in these formulas are $\mathcal O_E$-submodules.

There exist $a\ge0$, a strictly increasing flag $0=S_0\subsetneq\cdots\subsetneq S_a=U_{<1/2}$, and strictly increasing numbers $0<\tau_0<\cdots<\tau_{a-1}<1/2$, such that $$S_{i+1}=U_{\le\tau_i},\qquad s(S_{i+1}/S_i)=\tau_i,$$ and every $U_{\le t}$ with $t<1/2$ is a member of the flag. Equations indexed by $i$ use $0\le i<a$; when $a=0$, the list of $\tau_i$ is empty. For flags satisfying these conditions, the ordered lists of rank increments $r(S_{i+1})-r(S_i)$ and numbers $\tau_i$ are unique. Every such flag also satisfies $$S_i=U_{<\tau_i},\qquad r(S_i)<r(S_{i+1}),\qquad s_{\max}(S_{i+1})=\tau_i.$$ For every $S_i\subsetneq N\subseteq\Lambda$ one has $\tau_i\le s(N/S_i)$. For every $S_i\subseteq N\subsetneq S_{i+1}$ saturated in $S_{i+1}$, one has $s(S_{i+1}/N)\le\tau_i$. If $n\ge1$, then $a=0$ exactly when $s_{\min}\ge1/2$, and $a>0$ implies $\tau_0=s_{\min}$.
