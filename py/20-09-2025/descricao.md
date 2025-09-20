# Estudo de Caso — Sistema de Controle de Alarme com Portas Lógicas

Este estudo de caso expande a ideia de um sistema de alarme em uma fábrica, utilizando **portas lógicas** e simulação em **Python**. O desafio foi dividido em quatro níveis de complexidade, permitindo que o aluno avance passo a passo.

---

## Contexto

Uma fábrica precisa de um **sistema de alarme** que garanta a segurança em situações de risco. O alarme pode ser disparado por diferentes condições, que combinam sensores e controles de emergência.

As entradas possíveis são:

- **F (Fumaça):** 1 se há fumaça, 0 caso contrário.
- **B (Botão de Emergência):** 1 se pressionado, 0 caso contrário.
- **C (Chave de Segurança):** 1 se ativada, 0 caso contrário.
- **M (Movimento):** 1 se detectado movimento em área restrita, 0 caso contrário.

A saída é:

- **Alarme (A):** 1 se deve tocar, 0 caso contrário.

---

## Regras do Sistema

1. Se **há fumaça** (F = 1), o alarme toca.
2. Se **o botão de emergência** (B = 1) **e a chave de segurança** (C = 1) estão ativos, o alarme toca.
3. Se **há movimento em área restrita** (M = 1) **e não há chave de segurança** (C = 0), o alarme toca.

## Desafio

1. Resolver o **Nível 1** (só fumaça).
2. Expandir para o **Nível 2** (fumaça OU botão + chave).
3. Completar o **Nível 3** (incluindo movimento sem chave).
4. Implementar o **Nível 4** em Python e verificar todas as combinações de entradas.