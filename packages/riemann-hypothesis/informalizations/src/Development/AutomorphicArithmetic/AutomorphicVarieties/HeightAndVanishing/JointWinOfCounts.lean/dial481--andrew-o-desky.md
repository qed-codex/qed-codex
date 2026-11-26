---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/JointWinOfCounts.lean",
  "declarations": [
    "UpperTheory.V.HV.pointHV_of_counts"
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

## Positive localization lengths from character estimates

[Theorem GC.0079](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.pointHV_of_counts/)

Assume the condition in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), the assertions of ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)) and ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)), the condition in ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)) with a fixed real constant, and the five character estimates specified in the conventions below. Let $\psi$ be any primitive Dirichlet character, of conductor $N_\psi$, and let $j:\mathbb N\to\mathbb N$ be any function. There are natural numbers $C,r_1,r_2$, with $r_1,r_2$ prime, chosen before the following parameters.

Choose $\nu\ge2$, primes $q,d$ with $q\equiv3\pmod8$, $d\equiv7\pmod{16}$ and $(qd,N_\psi)=1$, an integer $t\ge2$, and $B\ge0$. Put $$N=\operatorname{lcm}(2^{\nu+2},N_\psi)qd,\qquad E=\mathbb Q(\mu_{2^{\nu+2}})^+K_\psi\mathbb Q(\sqrt{-q},\sqrt{-d}),$$ where $K_\psi$ is the field cut out by $\psi$. Require $q,d>2t+1$ and require that both $q,d$ exceed every member of $$N_\psi,\ o,\ p_K,\ h_K,\ p_1,\ r_1,\ r_2,$$ with the first five constants defined below. Suppose that for each $\ell\in\mathcal B_\psi$, every cyclotomic layer $L'/\mathbb Q(\mu_{\ell N_\psi})$ of degree $\ell^{j(\ell)}$ satisfies $$\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(L')\le B,$$ with all the individual lengths finite. Then the eigenspace $\mathcal S_{\ell,r}(E)^+$ on which natural complex conjugation acts by $(-1)^r$ has finite length for every odd prime $\ell$ and $1\le r<t$, and for every finite set $\mathcal P$ of odd primes, $$\sum_{\ell\in\mathcal P}\log\ell\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)^+\le(Nt)^C+CB.$$ All assumptions and conclusions concerning cohomology are uniform in algebraic closures and compatible local coefficient data. The group $\mathcal S$ is the localization kernel defined in ([Bound for localization kernels](https://andrewodesky.com/rh/lean/UpperTheory.One.vwin_of_row/)).
