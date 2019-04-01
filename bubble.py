from data import DataSeq

def Bubble(ds):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    for i in range(Length-1, -1, -1):
        for j in range(0, i, 1):
            if ds.data[j] > ds.data[j+1]:
                ds.Swap(j, j+1)

if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    Bubble(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()