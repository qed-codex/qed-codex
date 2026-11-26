---
{
  "module": "src/Formalism/LocalToGlobal/UnitaryNorms/CharDiv.lean",
  "declarations": [
    "Formalism.L2.Host.DivisorCharacterCompatibility"
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

## Local ratios and divisor character comparisons

[Definition / hypothesis ARAK.D200](https://andrewodesky.com/rh/lean/Formalism.L2.JointsSAlt/)

Use ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)), ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)), ([Compatibility of normalized Galois and theta data](https://andrewodesky.com/rh/lean/Formalism.L2.NTiedAllAlt/)) and ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)). Write $\mathbb A_{E/F}=\mathbb A_F\otimes_F E$, $\bar x$ for CM conjugation, and $x_f$ for its finite part. Put $\xi_0=-1/(N\mathfrak c\,s_d)$, using the ideal and square root in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)); write $\mathfrak p_k$ and $\omega_k$ for the chosen quadratic prime and character in ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)), and $\pi_k=\pi_{g,k}$ for the generator of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)). Write $\psi_{0,k,v}$ for its residue additive character $\psi_{k,v}$. A prime idempotent $e_P$ is the supported adelic idempotent of ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)). For $a\in E$ put $a_P=1+e_P(a-1)$.

Hypothesis (local ratios). For every finite $E$-prime $P$, every such $e_P$, $a\in E^\times$ and $y\in\mathbb A_{E/F}$ satisfying $y\overline{a_P}=a_P$, and every finite adelic one-dimensional unitary element $x$ whose determinant is $y_f$ (with the tensor factors exchanged), require $$d(x)=d_{\rm chr}(a\text{ supported at }P).$$ Here $d$ is the determinant homomorphism of the class-sum datum and $d_{\rm chr}$ is its Hecke-character determinant identification, both in ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)). Require $\bar\pi_k$ to be the image of an integer of the designated quadratic subfield lying in $\mathfrak p_k$, for $k=0,1$.

At every $F$-prime $v\mid g_k$, every $0\le j<m$ and every natural number $n$ coprime to $g_k$, require the selected residue character to satisfy $$\chi_{k,v,j}(n\bmod v)=\omega_k(n\bmod g_k)^{2(j+1)}.$$ The characters $\chi_{k,v,j}$ and local map $\phi_{k,v}$ are those of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)); $\omega_k$ is the character of ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). For every adelic $F$-idempotent $\epsilon_v$ supported at $v$ and all $c,y\in\mathcal O_F$ with $|c-\phi_{k,v}(\xi_0)|_v<1$, require $$\psi_{0,k,v}(y\bmod v)=\psi\left(\epsilon_v\frac{cy}{g_k}\right),$$ where $\psi$ is the additive character in ([Abstract oscillator representations and theta maps](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.AllTied/)) and reduction in the local field is zero outside its integer ring.

Hypothesis (divisor ramification). For every twist $\mu$, its designated set $Q_p(\mu)$ of natural numbers consists exactly of rational primes $p$ with an $E$-prime above $p$ at which $\xi_\mu$ is ramified. Its divisor-place index set $Q_{\rm pl}(\mu)$ has a chosen bijection with the $F$-primes below at least one such ramified $E$-prime. Under this bijection its recorded weight $q_v$ is exactly the absolute norm of that $F$-prime. These conditions concern the divisor index sets and weights of ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)) and the Hecke characters of ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)).
