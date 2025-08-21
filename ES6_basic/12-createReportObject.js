export default function createReportObject(employeesList) {
  const result = {
    allEmployees: employeesList,
    getNumberOfDepartments(departements) {
      return Object.keys(departements).length;
    },
  };

  return result;
}
