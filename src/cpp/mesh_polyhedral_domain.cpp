#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Mesh_triangulation_3.h>
#include <CGAL/Mesh_complex_3_in_triangulation_3.h>
#include <CGAL/Mesh_criteria_3.h>
#include <CGAL/Polyhedral_mesh_domain_3.h>
#include <CGAL/make_mesh_3.h>
#include <CGAL/refine_mesh_3.h>
// IO
#include <CGAL/IO/Polyhedron_iostream.h>
#include <write_c3t3_to_vtk_xml_file.h>
// Domain
typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Polyhedron_3<K> Polyhedron;
typedef CGAL::Polyhedral_mesh_domain_3<Polyhedron, K> Mesh_domain;
//Parallel
  typedef CGAL::Mesh_triangulation_3<
    Mesh_domain,
    CGAL::Kernel_traits<Mesh_domain>::Kernel, // Same as sequential
    CGAL::Parallel_tag                        // Tag to activate parallelism
  >::type Tr;
// Triangulation
// #ifdef CGAL_CONCURRENT_MESH_3
  // typedef CGAL::Mesh_triangulation_3<
    // Mesh_domain,
    // CGAL::Kernel_traits<Mesh_domain>::Kernel, // Same as sequential
    // CGAL::Parallel_tag                        // Tag to activate parallelism
  // >::type Tr;
// #else
  // typedef CGAL::Mesh_triangulation_3<Mesh_domain>::type Tr;
// #endif
typedef CGAL::Mesh_complex_3_in_triangulation_3<Tr> C3t3;
// Criteria
typedef CGAL::Mesh_criteria_3<Tr> Mesh_criteria;
// To avoid verbose function and named parameters call
using namespace CGAL::parameters;


int main( int argc, char* argv[])
{
    if( argc < 3 )
    {
        std::cerr << "Usage: "<< std::endl;
        std::cerr << argv[0];
        std::cerr << " <InputFileName>";
        std::cerr << " <OutputFileName>";
        std::cerr << " [FacetAngle]";
        std::cerr << " [FacetSize]";
        std::cerr << " [FacetDistance]";
        std::cerr << " [EdgeRatio]";
        std::cerr << " [ElementVolume]";
        std::cerr << std::endl;
        return EXIT_FAILURE;
    }

    const char * inputFile = argv[1];
    const char * outFile = argv[2];
    double facetAngle = 15;
    if(argc > 3)
      {
        facetAngle = atof(argv[3]);
      }
    double facetSize = 1.0;
    if(argc > 4)
      {
        facetSize = atof(argv[4]);
      }
    double facetDistance = 0.01;
    if(argc > 5)
      {
        facetDistance = atof(argv[5]);
      }
    double edgeRatio = 3.0;
    if(argc > 6)
      {
        edgeRatio = atof(argv[6]);
      }
    double elementVolume = 1.0;
    if(argc > 7)
      {
        elementVolume = atof(argv[7]);
      }
    // Create input polyhedron
    Polyhedron polyhedron;
    std::ifstream input(inputFile);
    input >> polyhedron;
    // Create domain
    Mesh_domain domain(polyhedron);
    // Mesh criteria (no cell_size set)
    Mesh_criteria criteria(facet_angle=facetAngle, facet_size=facetSize, facet_distance=facetDistance,
                           cell_radius_edge_ratio=edgeRatio, cell_size=elementVolume);
    // Mesh generation
    C3t3 c3t3 = CGAL::make_mesh_3<C3t3>(domain, criteria, odt(time_limit=30), perturb(sliver_bound=facetAngle, time_limit=60));
    // Set tetrahedron size (keep cell_radius_edge_ratio), ignore facets
    //Mesh_criteria new_criteria(cell_radius_edge_ratio=edgeRatio, cell_size=elementVolume);
    // Mesh refinement
    //CGAL::refine_mesh_3(c3t3, domain, new_criteria, perturb(sliver_bound=20, time_limit=60));
    // Output
    c3t3.remove_far_points();
    write_c3t3_to_vtk_xml_file(c3t3, outFile);
    return 0;
}
