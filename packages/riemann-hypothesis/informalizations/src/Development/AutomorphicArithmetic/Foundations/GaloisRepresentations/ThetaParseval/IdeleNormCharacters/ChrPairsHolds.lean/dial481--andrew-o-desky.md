---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/IdeleNormCharacters/ChrPairsHolds.lean",
  "declarations": [
    "UpperTheory.Gal.TP.Chr.chrEx_holds"
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

## CM characters with prescribed odd infinity exponents

[Theorem ANT.1459](https://andrewodesky.com/rh/lean/UpperTheory.Gal.TP.Chr.chrEx_holds/)

Let $E/F$ be the CM extension defined by a CM field and its maximal real subfield, unramified at every finite place. Choose an embedding $\tau_w:E\to\mathbb C$ over each infinite place $w$ of $F$, a finite place $w_0$ of $E$, and odd integers $m_w$. There are a unitary Hecke character $\chi$ of $\mathbb A_E^\times/E^\times$ and Hecke characters $\psi_{k,s}$ for every $k\ge0$, $s\in\mathbb Z$, such that $\chi$ is unramified at $w_0$ and its infinite component is $$\chi_\infty(z)=\prod_w\left(\frac{z_{\tau_w}}{|z_{\tau_w}|}\right)^{m_w}.$$ Every $\chi^k$ is continuous and trivial on principal $E$-ideles and restricts on $\mathbb A_F^\times$ to the $j$th power of the quadratic character of $E/F$ whenever $j\ge0$ and $j\equiv k\pmod2$.

For every finite place $v$, $$\psi_{k,s}\text{ is unramified at }v\ \Longleftrightarrow\ \chi^k\text{ is unramified at }v,$$ $$\psi_{k,s}(v)=\chi(v)^k(Nv)^{-s/2}.$$ The local value at $v$ is evaluation at the chosen uniformizer in $E_v$, also when the character is ramified. If $k+s$ is even, the positive infinity exponents of $\psi_{k,s}$ at $\tau_w,\overline{\tau_w}$ are respectively $$\frac{s+km_w}{2},\qquad\frac{s-km_w}{2}.$$ Finally, $\psi_{k,s}=\psi_{k',s'}$ implies $k=k'$.
