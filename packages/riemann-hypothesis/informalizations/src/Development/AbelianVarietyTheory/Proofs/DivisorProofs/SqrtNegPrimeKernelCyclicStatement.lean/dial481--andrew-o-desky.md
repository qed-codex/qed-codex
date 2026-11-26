---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/SqrtNegPrimeKernelCyclicStatement.lean",
  "declarations": [
    "GlobalTheory.T.sqrtNegPrime_kernel_cyclic"
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

## The kernel of an imaginary quadratic prime multiplier

[Theorem ANT.1080](https://andrewodesky.com/rh/lean/GlobalTheory.T.sqrtNegPrime_kernel_cyclic/)

Let $p>3$ be prime with $p\equiv3\pmod4$, and let $F\subseteq\mathbb C$ be a subfield containing $\mathbb Q$. Let $\omega_1,\omega_2\in\mathbb C$ be linearly independent over $\mathbb R$, and put $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$. Let $g_2(\Lambda)$ and $g_3(\Lambda)$ be the invariants defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)). Put $\alpha=i\sqrt p$, where $\sqrt p$ is the positive real square root. Assume $\alpha\Lambda\subseteq\Lambda$, $g_2(\Lambda),g_3(\Lambda)\in F$, and let $t\in\mathbb C$ satisfy $t\notin\Lambda$ and $\alpha t\in\Lambda$. Then $$kt\in\Lambda\ \Longleftrightarrow\ p\mid k\qquad(k\in\mathbb Z).$$ Every $z\in\mathbb C$ with $\alpha z\in\Lambda$ is congruent modulo $\Lambda$ to $kt$ for some $k\in\mathbb N$ with $k<p$. Moreover $\{kt:k\in\mathbb N,\ 1\le k<p\}$ consists of nonzero kernel representatives, no two congruent modulo $\Lambda$, and represents every nonzero class in $\ker(\alpha:\mathbb C/\Lambda\to\mathbb C/\Lambda)$.
