---
{
  "module": "src/Formalism/LocalToGlobal/NormalizedHeckeFactors/Choice.lean",
  "declarations": [
    "Formalism.L2.ExpGood",
    "Formalism.L2.ExpHyp",
    "Formalism.L2.NChoiceTied"
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

## Compatible choices of normalized twists

[Definition / hypothesis GC.D232](https://andrewodesky.com/rh/lean/Formalism.L2.NChoiceTied/)

Use ([Integral and theta compatibility for families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Extra/)), ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)), ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)), ([Local coefficient rings and normalized twists](https://andrewodesky.com/rh/lean/Formalism.L2.TwFrame/)) and ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)). Write $C_w=(i_w,Q_w,k_w,\psi_w)$ for the chosen twist data at a coefficient prime, with side $b_w$, coefficient extension $O_w'$ and embedding $K\to\operatorname{Frac}(O_w')$. Call $w$ twisted when $\mu_w\ne\mu_0$. Its effective character is $\psi_w$ on the true side and $\psi_w^{-1}$ on the false side.

Hypothesis (compatible normalized choices). Conjugate coefficient primes have the same twist index. At every twisted $w$, the selected side embedding of $K_0$ induces $w$: for $x\in K_0$, its $w$-valuation is nonnegative exactly when its image under that side belongs to $O_{i_w}^0$. The chosen embedding $K\to\operatorname{Frac}(O_w')$ restricts to this side embedding followed by the prescribed coefficient extension. Distinct conjugate twisted primes have opposite sides. Their effective choices $(i,Q,k,\psi^{\rm eff})$ are equal.

For any two twisted primes with the same index, their un-oriented choices have the same $Q$ and $k$, and $$\psi_{w'}=\psi_w^a\qquad\text{for some }a\in\mathbb Z\text{ with }(|a|,\ell_{i_w})=1.$$

The final condition is conditional on the following four hypotheses for the index $i$.

First assume the all-powers integral-twist existence assertion: for every index represented at a nonbase coefficient prime, satisfying the spectral conditions below, every $\epsilon>0$, every selected finite expansion basis of full rank at every stage and side, and every finite avoidance set $A$, there is one $(Q,k,\psi)$ for which every prime-to-$\ell_i$ integer power $\psi^a$ satisfies the full good-twist conditions. These are the six admissibility, integral-lattice, relative-index, Selmer-length, abelian-theta-value and ramification conditions of ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)), with $\epsilon$ replacing $\ell_i^{-2}$ and $A$ added to the forbidden primes. One choice of $Q,k,\psi$ works for every such power.

Second, the true-side base coefficient prime is the restriction of some nonbase coefficient prime: on integral $x\in K_0$, membership of its image in the maximal ideal of $O_i^0$ is equivalent to strict positivity of that prime's valuation.

Third, impose these spectral conditions. A spectral label is selected if some nonzero theta vector fixed by the designated idempotent has all its recorded split Hecke eigenvalues. For each selected label put $T_s=\rho_s\chi_s^{-1}$, with $\chi_s$ the first normalizing character. There is one integral invertible matrix $A_s$ such that, for every $g\in G_E$, $$\epsilon_\ell(cgc^{-1})\,T_s(cgc^{-1})^{-\mathsf T}=A_s\,\epsilon_\ell(g)^tT_s(g)\,A_s^{-1}.$$ At every prime above $\ell_i$ and every induced coefficient embedding, the filtered local period representation of $T_s$ has no jump in $[-1,t]$: every integer jump $a$ satisfies $a<-1$ or $t<a$. A jump means a nonzero associated graded piece of its specified period filtration. The untwisted sum of the abelian theta coefficients is nonzero for every abelian label $\lambda$. There is an integer $s$ with $$s_{i,\lambda}=2s,\qquad1\le s\le k+m(t+s_*+1)+1,$$ where $s_*=r+6$ if $r+6$ is odd and $s_*=r+7$ otherwise. Also $r\ge100$ and $g_0,g_1\ge2r$.

Fourth, at every selected stage and side, the designated finite expansion subset is an integral basis of the scaled-idempotent module and that module has full fraction-field rank, exactly as in ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)).

Whenever all four hypotheses hold, the effective chosen twist at every twisted prime with index $i$ satisfies all six good-twist conditions with $\epsilon=\ell_i^{-2}$. Its auxiliary set also avoids every prime over $$\{2,3,5,\ell_i,g_0,g_1,p_\Delta,p'_\Delta,q_0\}\cup\{T_u:u\text{ a source}\}\cup\{p:p\mid N\mathfrak c_{E_0}\,|\operatorname{disc}E|\}.$$ The quantities $N_0(i)$ and the selected expansion subsets are those fixed in ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)); the conditional assertion introduces no new thresholds or bases.
