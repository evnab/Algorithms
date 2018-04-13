import com.williamfiset.algorithms.sorting.BubbleSort;

import static org.junit.Assert.*;
import org.junit.*;
import java.util.*;

public class BubbleTest {

    @Test
    public void noLongestCommonSubstringTest() {
        int[] outOfOrder = {9,8,5,3,7,9};
        BubbleSort.bubbleSort(outOfOrder);

    }
}
