// Here's an example implementation of the Sorter class using the Strategy Pattern:

public class Sorter {
    private SortingAlgorithm sortingAlgorithm;

    public Sorter(SortingAlgorithm sortingAlgorithm) {
        this.sortingAlgorithm = sortingAlgorithm;
    }

    public void setSortingAlgorithm(SortingAlgorithm sortingAlgorithm) {
        this.sortingAlgorithm = sortingAlgorithm;
    }

    public void sort(int[] arr) {
        sortingAlgorithm.sort(arr);
    }
}

interface SortingAlgorithm {
    void sort(int[] arr);
}

class QuickSort implements SortingAlgorithm {
    @Override
    public void sort(int[] arr) {
        System.out.println("Sorting using Quick Sort");
        // implementation of Quick Sort algorithm
    }
}

class MergeSort implements SortingAlgorithm {
    @Override
    public void sort(int[] arr) {
        System.out.println("Sorting using Merge Sort");
        // implementation of Merge Sort algorithm
    }
}


// To use the Sorter class, we can create an instance of it with a specific SortingAlgorithm, and then call its sort method:
Sorter sorter = new Sorter(new QuickSort());
int[] arr = {4, 2, 5, 1, 3};
sorter.sort(arr); // Sorting using Quick Sort

sorter.setSortingAlgorithm(new MergeSort());
sorter.sort(arr); // Sorting using Merge Sort
