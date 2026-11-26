---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/OddResidueBounds/ThmBcOfPsiBound.lean",
  "declarations": [
    "UpperTheory.V.Odd.stickBound",
    "UpperTheory.V.Odd.thmBcFree_of"
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

## Summing the negative localization lengths

[Theorem GC.0087](https://andrewodesky.com/rh/lean/UpperTheory.V.Odd.thmBcFree_of/)

Assume the character-eigenspace bound specified below. There is a real constant $C_-$ with the following property. Let $F\subseteq\mathbb Q(\mu_m)$ be an abelian field given by a fixing subgroup, and put $o=[F:\mathbb Q]$. Let $\nu,t\ge2$, and let $q,d$ be primes with $q\equiv3\pmod8$, $d\equiv7\pmod{16}$ and $(qd,m)=1$. Let $$E=F\mathbb Q(\mu_{2^{\nu+2}})^+\mathbb Q(\sqrt{-q},\sqrt{-d})$$ be a CM field, put $n=[E:\mathbb Q]$, and let $F_E$ be its cyclotomic conductor, the least positive integer $M$ for which $E$ embeds in $\mathbb Q(\mu_M)$. For every odd prime $\ell$ and $1\le r<t$, the eigenspace $\mathcal S_{\ell,r}(E)^-$ on which natural complex conjugation acts by $(-1)^{r+1}$ has finite length. For every finite set $\mathcal P$ of odd primes, $$\sum_{\ell\in\mathcal P}\log\ell\sum_{1\le r<t}\operatorname{length}_{\mathbb Z_\ell}\mathcal S_{\ell,r}(E)^-\le3nt^2\log(tF_E)+C_-\sum_{\substack{\ell\mid o\\\ell\text{ odd prime}}}\ell n^2t^2\bigl(\log(t\ell F_E)\bigr)^2.$$ The assertions are uniform in the algebraic closure and compatible local coefficient data. Here $\mathcal S$ is the localization kernel defined in ([Bound for localization kernels](https://andrewodesky.com/rh/lean/UpperTheory.One.vwin_of_row/)).

## A uniform bound for an odd localization kernel

[Theorem GC.1294](https://andrewodesky.com/rh/lean/UpperTheory.V.Odd.stickBound/)

There is an absolute constant $C\ge0$ with the following property. Let $E$ be a CM number field, let $N\ge1$, and suppose that there is a $\mathbb Q$-embedding $E\hookrightarrow\mathbb Q(\mu_N)$. Fix an algebraic closure $\Omega$ of $E$, a prime $\ell$, and the following localization data: all finite places $S$ above $\ell$, a choice of an extension to $\Omega$ of each such place, and the cyclotomic character descended to the Galois group $G_{E,S}$ unramified outside $S$. Assume that $\ell\ne2$, or that $G_E$ acts trivially on $\mu_4$.

For an integer $e\ge1$, let $$\mathcal K_e=\ker\left(H^1(G_{E,S},(\mathbb Q_\ell/\mathbb Z_\ell)(-e))\longrightarrow\prod_{v\mid\ell}H^1(E_v,(\mathbb Q_\ell/\mathbb Z_\ell)(-e))\right).$$ Let $\mathcal K_e^-$ be the submodule on which the natural complex-conjugation action on this cohomology is multiplication by $(-1)^{e+1}$. Then $\lambda_e=\operatorname{length}_{\mathbb Z_\ell}\mathcal K_e^-$ is finite and $$\lambda_e\log\ell\le C\ell[E:\mathbb Q]^2(e+1)\bigl(\log(e\ell N)\bigr)^2.$$ The constant is independent of the field, conductor, twist, prime, and localization choices.
