package pkgUT;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.LocalDate;

import org.apache.poi.ss.formula.functions.FinanceLib;
import org.junit.jupiter.api.Test;

import pkgLogic.Loan;

public class testEscrow {

	@Test
	public void testEscrow() {
		LocalDate date = LocalDate.now();
		Loan l = new Loan(40000,0.68,20,date,100,123.456);
		double escrow = 123.456;
		assertEquals(123.456,l.getEscrow());
	}
		

}

