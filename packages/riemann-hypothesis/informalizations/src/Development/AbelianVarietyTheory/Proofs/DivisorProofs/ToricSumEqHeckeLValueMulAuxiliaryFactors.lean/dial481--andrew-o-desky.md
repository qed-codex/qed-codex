---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToricSumEqHeckeLValueMulAuxiliaryFactors.lean",
  "declarations": [
    "GlobalTheory.ToricSumValue.toricSum_eq"
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

## A toric lattice sum as a Hecke L-value

[Theorem ANT.1702](https://andrewodesky.com/rh/lean/GlobalTheory.ToricSumValue.toricSum_eq/)

Assume that for every CM number field and CM type, every unitary Hecke character whose archimedean part on $x\in E^\times$ is $\prod_i(\phi_i(x)/|\phi_i(x)|)^{2m_i}$ for integers $m_i$ with at least one $m_i\ne0$, admits an entire function agreeing with its Euler product on $\Re z>1$. Let $E$ be a CM number field with maximal real subfield $F$, CM type $(\phi_i)_{i\in I}$, $s\ge1$, and $\kappa\in\mathbb N^I$. Assume $E/F$ is unramified at finite places. Let $\mathfrak f$ be a nonzero proper ideal of $\mathcal O_F$ whose prime divisors split in $E$ and have exponent at most two; each lies over an odd $\ell\nmid\operatorname{disc}E$ with all primes of $E$ over $\ell$ of norm $\ell$. Let $Q$ be a finite set of split primes of $F$ not dividing $\mathfrak f$.

Let $\chi$ be unitary, with the product of its local restrictions above each place of $F$ trivial on $F^\times$, and with archimedean part on $x\in E^\times$ equal to $\prod_i(\phi_i(x)/|\phi_i(x)|)^{2(\kappa_i+s)}$. Above $v\notin Q$, assume its exact conductor exponent equals the exponent of $v$ in $\mathfrak f$; above $v\in Q$, assume its conductor exponent is at most one. Choose a prime $P_q$ of $E$ above every $q\in Q$, and let $L(z,\chi)$ be an entire function agreeing with the Hecke Euler product on $\Re z>1$.

Put $\mathfrak c=\mathfrak f\prod_{q\in Q}q$ and $\mathcal O_{\mathfrak c}=\mathcal O_F+\mathfrak c\mathcal O_E$. The group $$\operatorname{Pic}(\mathcal O_{\mathfrak c})=\mathbb A_{E,f}^\times/(E^\times\widehat{\mathcal O_{\mathfrak c}}^{\times})$$ is finite. For the prescribed representative $y$ of each class there is an entire $S_y$ given on $\Re z>1-s$ by $$S_y(z)=\sum_{x\in(E\cap y\widehat{\mathcal O_{\mathfrak c}})\setminus\{0\}\,/\,\mathcal O_F^\times}\prod_i\phi_i(x)^{-(2s+\kappa_i)}\overline{\phi_i(x)}^{\kappa_i}|\phi_i(x)|^{-2z}.$$ These functions satisfy $$\sum_{[y]}\frac{S_y(0)}{\chi_f(y)|y|_f^s} =L(s,\chi)\prod_{\substack{q\in Q\\\chi\ \mathrm{unramified\ at}\ P_q}} \left[(1-\alpha_q(Nq)^{-s})(1-\alpha_q^{-1}(Nq)^{-s})+(Nq-1)(Nq)^{-2s}\right].$$ Here $\chi_f$ is the finite part, $|y|_f$ the finite idele norm, $Nq=|\mathcal O_F/q|$, and $\alpha_q=\chi_{P_q}(\varpi_{P_q})$, where $\varpi_{P_q}$ is the fixed uniformizer of normalized additive valuation one and $\chi_{P_q}$ is the local character specified in ([Unique finite local component of a Hecke character](https://andrewodesky.com/rh/lean/GlobalTheory.HeckeComp.main/)).
