def main():
    N, M = map(int, input().split())
    result, parties = [0] * M, []
    truth = list(map(int, input().split()))
    truth = set(truth[1:]) if len(truth) >= 2 else set()
    for _ in range(M):
        party = list(map(int, input().split()))
        parties.append(party[1:])
    for _ in range(M):
        for p_idx, party in enumerate(parties):
            if truth.intersection(party):
                truth = truth.union(set(party))
                result[p_idx] = 0
            else:
                result[p_idx] = 1
    return sum(result)


if __name__ == "__main__":
    print(main())
